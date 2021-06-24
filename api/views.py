from rest_framework import generics

from user.models import CustomUser
from .serializers import UserWithDepthSerializer, UserSerializer


class DoctorList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(type="D")
    serializer_class = UserWithDepthSerializer


class UserDetails(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserWithDepthSerializer


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
