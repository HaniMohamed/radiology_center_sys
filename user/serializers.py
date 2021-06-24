from rest_framework import serializers

from user.models import CustomUser


class UserWithDepthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'first_name', 'last_name', 'sex', 'age', 'blood_type', 'department', 'phone', 'address',
            'notes')
        model = CustomUser
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'first_name', 'last_name', 'sex', 'age', 'blood_type', 'department', 'phone', 'address',
            'notes')
        model = CustomUser
