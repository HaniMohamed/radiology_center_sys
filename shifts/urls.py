from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShiftList.as_view(), name='shift_list'),
    path('new', views.ShiftCreate.as_view(), name='shift_new'),
    path('<int:pk>', views.ShiftDetail.as_view(), name='shift_detail'),
    path('update/<int:pk>', views.ShiftUpdate.as_view(), name='shift_update'),
    path('delete/<int:pk>', views.ShiftDelete.as_view(), name='shift_delete'),
]
