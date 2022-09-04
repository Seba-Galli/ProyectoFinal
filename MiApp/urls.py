from django.urls import path
from MiApp.views import entrada, estacionamiento, salida, inicio

urlpatterns = [
    path('', inicio, name='MiAppInicio'),
    path('estacionamiento/', estacionamiento, name='AppEstacionamiento'),
    path('entrada/', entrada, name='AppEntrada'),
    path('salida/', salida, name='AppSalida'),
]