from rest_framework import serializers

from .models import Radiology


class RadiologySerializer(serializers.ModelSerializer):
    class Meta:
        fields = fields = '__all__'
        model = Radiology
