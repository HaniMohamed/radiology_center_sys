from django.db import models

from user.models import Doctor, Patient


# Create your models here.

class Radiology(models.Model):
    name = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    price = models.IntegerField()
    medical_insurance_discount = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Examination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient
