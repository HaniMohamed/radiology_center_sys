from django.contrib.auth.models import AbstractUser
from django.db import models

from departments.models import BloodType, Department


class CustomUser(AbstractUser):
    TYPE_CHOICES = [
        ('R', 'Receptionist'),
        ('D', 'Doctor'),
        ('P', 'Patient'),
        ('A', 'Admin'),
    ]
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    type = models.CharField(max_length=1,
                            choices=TYPE_CHOICES,
                            default="R", )
    phone = models.CharField(max_length=11, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=1,
                           choices=SEX_CHOICES,
                           default="M", )
    age = models.IntegerField(blank=True, null=True)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)



# class Doctor(models.Model):
#     name = models.CharField(max_length=30)
#     phone = models.CharField(max_length=11)
#     email = models.EmailField(max_length=50)
#     address = models.TextField()
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     notes = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name


# class Patient(models.Model):
#     SEX_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#     ]
#
#     name = models.CharField(max_length=30)
#     phone = models.CharField(max_length=11)
#     age = models.IntegerField()
#     sex = models.CharField(max_length=1,
#                            choices=SEX_CHOICES,
#                            default="M", )
#     blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
#     city = models.CharField(max_length=30)
#     notes = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name


# class Receptionist(models.Model):
#     SEX_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#     ]
#
#     name = models.CharField(max_length=30)
#     phone = models.CharField(max_length=11)
#     age = models.IntegerField()
#     sex = models.CharField(max_length=1,
#                            choices=SEX_CHOICES,
#                            default="M", )
#     address = models.TextField()
#     notes = models.TextField(default=" ")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
