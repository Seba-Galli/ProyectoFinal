from django.urls import path
from MiApp.views import entrada, estacionamiento, salida, inicio

urlpatterns = [
    path('', inicio),
    path('estacionamiento/', estacionamiento),
    path('entrada/', entrada),
    path('salida/', salida),
]