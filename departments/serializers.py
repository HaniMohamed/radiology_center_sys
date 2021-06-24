from rest_framework import serializers

from .models import Department
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Department
