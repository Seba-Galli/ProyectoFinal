from django.urls import path
from MiApp.views import inicio, estacionamiento, entrada, salida, estacion_form

urlpatterns = [
    path('', inicio, name='MiAppInicio'),
    path('estacionamiento/', estacionamiento, name='AppEstacionamiento'),
    path('entrada/', entrada, name='AppEntrada'),
    path('salida/', salida, name='AppSalida'),
    path('estacion_form/', estacion_form, name='AppEstacionamientoForm'),
]