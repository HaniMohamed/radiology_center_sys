from django.urls import path

from . import views

urlpatterns = [
    path('departments/', views.DepartmentList.as_view()),
    path('departments/create', views.DepartmentCreate.as_view()),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view()),

    # Doctors APIs
    path('doctors/', views.UserList.as_view()),
    path('doctors/create', views.UserCreate.as_view()),
    path('doctors/<int:pk>/', views.UserDetails.as_view()),
    path('doctors/<int:pk>/update', views.UserUpdate.as_view()),
    path('doctors/<int:pk>/delete', views.UserDelete.as_view()),


]
