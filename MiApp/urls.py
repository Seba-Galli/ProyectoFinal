from django.urls import path
from MiApp.views import inicio, estacionamiento, entrada, salida, estacion_form, busqueda_estac, busqueda_estac_post, eliminar_estacionamiento



urlpatterns = [
    path('', inicio, name='MiAppInicio'),
    path('estacionamiento/', estacionamiento, name='AppEstacionamiento'),
    path('entrada/', entrada, name='AppEntrada'),
    path('salida/', salida, name='AppSalida'),
    path('estacion_form/', estacion_form, name='AppEstacionamientoForm'),
    path('busqueda_estac/', busqueda_estac, name='AppBusquedaHora'),
    path('busqueda_estac_post/', busqueda_estac_post, name='AppBusquedaHoraPost'),
    path('eliminar_estacionamiento/<int:PrecioHora>', eliminar_estacionamiento, name='AppPrecioEliminar'),
]