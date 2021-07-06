# Create your views here.
from rest_framework import generics

from radiology.models import Radiology, Examination
from radiology.serializers import RadiologyWithDepthSerializer, ExaminationSerializer, ExaminationWithDepthSerializer


class RadiologyList(generics.ListCreateAPIView):
    queryset = Radiology.objects.all()
    serializer_class = RadiologyWithDepthSerializer


class RadiologyCreate(generics.CreateAPIView):
    queryset = Radiology.objects.all()
    serializer_class = RadiologyWithDepthSerializer


class RadiologyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Radiology.objects.all()
    serializer_class = RadiologyWithDepthSerializer


class ExaminationList(generics.ListCreateAPIView):
    queryset = Examination.objects.all()
    serializer_class = ExaminationWithDepthSerializer


class ExaminationDetails(generics.RetrieveDestroyAPIView):
    queryset = Examination.objects.all()
    serializer_class = ExaminationWithDepthSerializer


class ExaminationCreate(generics.CreateAPIView):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer


class ExaminationUpdate(generics.UpdateAPIView):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer


class ExaminationDelete(generics.DestroyAPIView):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
