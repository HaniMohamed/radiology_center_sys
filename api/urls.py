from django.urls import path

from .views import DepartmentList, DepartmentDetail, DoctorDetail, DoctorList

urlpatterns = [
    path('departments/', DepartmentList.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('doctors/', DoctorList.as_view()),
    path('doctors/<int:pk>/', DoctorDetail.as_view()),

]
