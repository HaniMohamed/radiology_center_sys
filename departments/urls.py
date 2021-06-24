
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DepartmentList.as_view(), name='department_home'),
    path('new/', views.DepartmentCreate.as_view(), name='department_new'),
    path('<int:pk>/', views.DepartmentDetail.as_view(), name='department_detail'),
]
