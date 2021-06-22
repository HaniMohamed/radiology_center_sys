from rest_framework import serializers

from departments.models import Department
from user.models import Doctor


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = fields = '__all__'
        model = Department


class DoctorWithDepthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = fields = '__all__'
        model = Doctor
        depth = 1


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Doctor
