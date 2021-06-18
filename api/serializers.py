from rest_framework import serializers

from departments.models import Department
from user.models import Doctor


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = fields = '__all__'
        model = Department


class DoctorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False)

    class Meta:
        fields = fields = '__all__'
        model = Doctor
