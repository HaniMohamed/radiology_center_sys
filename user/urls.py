
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.UserDetails.as_view(), name='user_details'),
    path('doctors', views.DoctorList.as_view(), name='doctors_list'),
    path('patients', views.PatientList.as_view(), name='patients_list'),
    path('receptionists', views.ReceptionistList.as_view(), name='receptionists_list'),
    path('new', views.UserCreate.as_view(), name='new_user'),
    path('update/<int:pk>', views.UserCreate.as_view(), name='update_user'),
    path('delete/<int:pk>', views.UserDelete.as_view(), name='delete_user'),
]
