from rest_framework import serializers

from departments.models import Department
from user.models import CustomUser



class UserWithDepthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = fields = '__all__'
        model = CustomUser
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CustomUser
