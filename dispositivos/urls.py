from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispositivos, name='dispositivos'),
]