from django.db import models

# Create your models here.
from django.db.models import ForeignKey

from user.models import CustomUser


class Shift(models.Model):
    receptionist = ForeignKey(CustomUser, on_delete=models.CASCADE, )
    total_income = models.DecimalField(max_digits=100, decimal_places=2, default=0.0)
    closed = models.BooleanField(default=False, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.receptionist.username
