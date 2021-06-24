
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.UserDetails, name='user_details'),
    path('doctors', views.DoctorList, name='doctors_list'),
    path('patients', views.PatientList, name='patients_list'),
    path('receptionists', views.ReceptionistList, name='receptionists_list'),
    path('new', views.UserCreate, name='new_user'),
    path('update/<int:pk>', views.UserCreate, name='update_user'),
    path('delete/<int:pk>', views.UserDelete, name='delete_user'),
]
