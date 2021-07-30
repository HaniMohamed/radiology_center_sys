
from rest_framework import serializers

from .models import Insurance


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Insurance

