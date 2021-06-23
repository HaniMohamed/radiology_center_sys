from django.contrib import admin

from .models import Doctor, Patient, Receptionist, CustomUser

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Receptionist)
# admin.site.register(CustomUser)
