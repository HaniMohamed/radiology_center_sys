from rest_framework import generics

from .models import CustomUser
from .serializers import UserWithDepthSerializer, UserSerializer


class DoctorList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(type="D").order_by('-created_at')
    serializer_class = UserWithDepthSerializer


class PatientList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(type="P").order_by('-created_at')
    serializer_class = UserWithDepthSerializer


class ReceptionistList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(type="R").order_by('-created_at')
    serializer_class = UserWithDepthSerializer


class UserDetails(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = UserWithDepthSerializer


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = UserSerializer
