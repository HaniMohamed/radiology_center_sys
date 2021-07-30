from django.db import models

from shifts.models import Shift
from user.models import CustomUser


# Create your models here.

class Radiology(models.Model):
    name = models.CharField(max_length=30)
    # doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, editable=True)
    medical_insurance_discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Examination(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="patient")
    supervisor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    another_supervisor = models.CharField(max_length=30, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    radiology = models.ManyToManyField(Radiology)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE, blank=True, null=True)
    actual_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.username
