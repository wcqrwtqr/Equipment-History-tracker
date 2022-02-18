from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobindex, name='jobindex'),
]
