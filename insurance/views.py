from rest_framework import generics

from .models import Insurance
from .serializers import InsuranceSerializer


class InsuranceList(generics.ListCreateAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class InsuranceCreate(generics.CreateAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class InsuranceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
