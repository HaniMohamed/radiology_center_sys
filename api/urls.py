from django.urls import path

from .views import DepartmentList, DepartmentDetail, DoctorRetrieveDestroy, DoctorList, DoctorCreate, DoctorUpdate

urlpatterns = [
    path('departments/', DepartmentList.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('doctors/', DoctorList.as_view()),
    path('doctors/create', DoctorCreate.as_view()),
    path('doctors/<int:pk>/', DoctorRetrieveDestroy.as_view()),
    path('doctors/<int:pk>/update', DoctorUpdate.as_view()),

]
