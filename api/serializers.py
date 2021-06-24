from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from departments.models import Department
from user.models import CustomUser


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = fields = '__all__'
        model = Department


class UserWithDepthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = fields = '__all__'
        model = CustomUser
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['user_type'] = self.user.type
        data['username'] = self.user.username

        data['refresh'] = str(refresh)
        data['access-token'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
