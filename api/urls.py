from django.urls import path

from auth import views as auth_views
from . import views

urlpatterns = [
    path('users/login/', auth_views.CustomTokenObtainPairView.as_view(), name='auth_login'),
    path('users/logout/', auth_views.LogoutView.as_view(), name='auth_logout'),

    path('departments/', views.DepartmentList.as_view()),
    path('departments/create', views.DepartmentCreate.as_view()),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view()),

    # Doctors APIs
    path('doctors/', views.DoctorList.as_view()),
    path('doctors/create', views.UserCreate.as_view()),
    path('doctors/<int:pk>/', views.UserDetails.as_view()),
    path('doctors/<int:pk>/update', views.UserUpdate.as_view()),
    path('doctors/<int:pk>/delete', views.UserDelete.as_view()),

]
