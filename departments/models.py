from django.db import models

# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=30)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # new
        return reverse('department_detail', args=[str(self.id)])


class BloodType(models.Model):
    name = models.CharField(max_length=30)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
