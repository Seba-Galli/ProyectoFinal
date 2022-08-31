
from django.contrib import admin
from django.urls import path

from MiApp.views import entrada, estacionamiento, salida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estacionamiento/', estacionamiento),
    path('entrada/', entrada),
    path('salida/', salida),
]
