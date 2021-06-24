from django.urls import path

from . import views

urlpatterns = [
    path('radiology', views.RadiologyList.as_view(), name='radiology_list'),
    path('radiology/new', views.RadiologyCreate.as_view(), name='radiology_new'),
    path('radiology/<int:pk>', views.RadiologyDetail.as_view(), name='radiology_detail'),
]
