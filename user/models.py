from django.db import models

from departments.models import Department, BloodType


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    sex = models.CharField(max_length=1,
                           choices=SEX_CHOICES,
                           default="M", )
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Receptionist(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    sex = models.CharField(max_length=1,
                           choices=SEX_CHOICES,
                           default="M", )
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
