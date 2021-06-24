from rest_framework import generics

from departments.models import Department
from user.models import CustomUser
from .serializers import DepartmentSerializer, UserWithDepthSerializer, UserSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreate(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
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
