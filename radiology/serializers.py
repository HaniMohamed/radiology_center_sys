from rest_framework import serializers

from .models import Radiology, Examination


class RadiologySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Radiology


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Examination


class ExaminationWithDepthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Examination
        depth = 1
