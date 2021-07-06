from rest_framework import serializers

from .models import Radiology, Examination


class RadiologyWithDepthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Radiology
        depth = 5


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Examination


class ExaminationWithDepthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Examination
        depth = 5
