from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

# Create your views here.
from shifts.models import Shift
from shifts.serializers import ShiftWithDepthSerializer, ShiftSerializer


class ShiftList(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftWithDepthSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['closed',]


class ShiftCreate(generics.CreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftWithDepthSerializer


class ShiftDetail(generics.RetrieveAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftWithDepthSerializer


class ShiftUpdate(generics.UpdateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftDelete(generics.DestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
