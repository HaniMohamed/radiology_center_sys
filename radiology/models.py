from django.db import models

from user.models import CustomUser


# Create your models here.

class Radiology(models.Model):
    name = models.CharField(max_length=30)
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, editable=True)
    medical_insurance_discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Examination(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="patient")
    supervisor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    radiology = models.ManyToManyField(Radiology)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient
