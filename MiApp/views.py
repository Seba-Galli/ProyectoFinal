from django.shortcuts import render

from .models import Entrada, Salida, Estacionamiento

def estacionamiento(request):
    estacionar = Estacionamiento(PrecioHora="300", hora_ingreso="2022-08-30 15:00:00", hora_egreso= "2022-08-30 17:00:00")
    contexto = {'estacionamiento': estacionar}
    estacionar.save()
    return render(request,"Apps/estacionamiento.html", contexto)

def entrada(request):
    entrar = Entrada(vehiculo="Auto", patente="ABC123", nombre="Sebastian")
    contexto = {'entrada': entrar}
    entrar.save()
    return render(request,"Apps/entrada.html", contexto)

def salida(request):
    salir = Salida(vehiculo="Auto", patente="ABC123", nombre="Sebastian")
    contexto = {'salida': salir}
    salir.save()
    return render(request,"Apps/salida.html", contexto)

def inicio(request):
    return render(request, 'index.html')


