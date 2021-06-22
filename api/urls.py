from django.urls import path

from . import views

urlpatterns = [
    path('departments/', views.DepartmentList.as_view()),
    path('departments/create', views.DepartmentCreate.as_view()),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view()),

    # Doctors APIs
    path('doctors/', views.DoctorList.as_view()),
    path('doctors/create', views.DoctorCreate.as_view()),
    path('doctors/<int:pk>/', views.DoctorDetails.as_view()),
    path('doctors/<int:pk>/update', views.DoctorUpdate.as_view()),
    path('doctors/<int:pk>/delete', views.DoctorDelete.as_view()),


]
