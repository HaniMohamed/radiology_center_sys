from django.urls import path

from .views import DepartmentList, DepartmentDetail, DoctorDetails, DoctorList, DoctorCreate, DoctorUpdate, DoctorDelete

urlpatterns = [
    path('departments/', DepartmentList.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),

    # Doctors APIs
    path('doctors/', DoctorList.as_view()),
    path('doctors/create', DoctorCreate.as_view()),
    path('doctors/<int:pk>/', DoctorDetails.as_view()),
    path('doctors/<int:pk>/update', DoctorUpdate.as_view()),
    path('doctors/<int:pk>/delete', DoctorDelete.as_view()),


]
