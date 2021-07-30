from django.urls import path, include

from auth import views as auth_views
from departments import views as department_views
from . import views

urlpatterns = [
    path('users/login/', auth_views.CustomTokenObtainPairView.as_view(), name='auth_login'),
    path('users/logout/', auth_views.LogoutView.as_view(), name='auth_logout'),

    path('departments/', include('departments.urls')),


    # users APIs
    path('users/', include('user.urls')),

    # shifts APIs
    path('shifts/', include('shifts.urls')),

    # radiology APIs
    path('', include('radiology.urls')),


]
