from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Radiology)
admin.site.register(models.Examination)
