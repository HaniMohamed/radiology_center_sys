from django.urls import path
from . import views

urlpatterns = [
    path('', views.InsuranceList.as_view(), name='iInsurance_list'),
    path('new', views.InsuranceCreate.as_view(), name='iInsurance_new'),
    path('<int:pk>', views.InsuranceDetail.as_view(), name='iInsurance_detail'),
]
