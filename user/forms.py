from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise CustomUser.ValidationError(self.error_messages['duplicate_username'])
