# Create your views here.
from rest_framework import generics

from radiology.models import Radiology
from radiology.serializers import RadiologySerializer


class RadiologyList(generics.ListCreateAPIView):
    queryset = Radiology.objects.all()
    serializer_class = RadiologySerializer


class RadiologyCreate(generics.CreateAPIView):
    queryset = Radiology.objects.all()
    serializer_class = RadiologySerializer


class RadiologyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Radiology.objects.all()
    serializer_class = RadiologySerializer
