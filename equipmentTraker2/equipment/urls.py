from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='equipment'),
    path('', views.equipmentListView.as_view(), name='equipment'),
    path('equipment/new/', views.equipmentCreateView.as_view(), name='equipment_new'),
]
