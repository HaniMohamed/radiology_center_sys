from rest_framework import serializers

from shifts.models import Shift


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Shift


class ShiftWithDepthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Shift
        depth = 5

