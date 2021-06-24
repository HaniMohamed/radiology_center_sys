from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserChangeForm, MyUserCreationForm
from .models import CustomUser


# Register your models here.
# admin.site.register(Doctor)
# admin.site.register(Patient)
# admin.site.register(Receptionist)
#

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('type', 'sex', 'blood_type')}),
    )


admin.site.register(CustomUser, MyUserAdmin)
