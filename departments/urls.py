
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='department_home'),
    path('new/', views.DepartmentCreateView.as_view(), name='department_new'),
    path('<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
]
