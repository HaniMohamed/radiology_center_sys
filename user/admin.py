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
    list_display = ('username', 'type', 'phone', 'department')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('type', 'sex', 'blood_type', 'department')}),
    )


admin.site.register(CustomUser, MyUserAdmin)
