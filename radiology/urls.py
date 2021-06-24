from django.urls import path

from . import views

urlpatterns = [
    # Radiology urls

    path('radiology', views.RadiologyList.as_view(), name='radiology_list'),
    path('radiology/new', views.RadiologyCreate.as_view(), name='radiology_new'),
    path('radiology/<int:pk>', views.RadiologyDetail.as_view(), name='radiology_detail'),

    # Examination urls
    path('examination', views.ExaminationList.as_view(), name='examination_list'),
    path('examination/new', views.ExaminationCreate.as_view(), name='examination_new'),
    path('examination/<int:pk>', views.ExaminationDetails.as_view(), name='examination_detail'),
    path('examination/update/<int:pk>', views.ExaminationUpdate.as_view(), name='update_examination'),
    path('examination/delete/<int:pk>', views.ExaminationDelete.as_view(), name='delete_examination'),
]
