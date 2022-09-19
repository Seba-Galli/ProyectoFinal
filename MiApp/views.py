from django.shortcuts import redirect, render

from MiApp.forms import Estac_Form, BusquedaEstacForm

from .models import Entrada, Estacionamiento, Salida

from django.contrib import messages


def eliminar_estacionamiento(request, PrecioHora):
    precio_eliminar = Estacionamiento.objects.get(PrecioHora=PrecioHora)
    precio_eliminar.delete()

    messages.info(request, f'El precio {precio_eliminar}, fue eliminado')

    return redirect('AppEstacionamiento')

def busqueda_estac_post(request):
    PrecioHora = request.GET.get('PrecioHora')

    estacionamientos = Estacionamiento.objects.filter(PrecioHora__icontains=PrecioHora)

    contexto = {
        'estacionamientos': estacionamientos
    }

    return render(request,"Apps/estacion_filtrado.html", contexto)

def busqueda_estac(request):
    contexto = {
        'form': BusquedaEstacForm()
    }

    return render(request, 'Apps/busqueda_estac.html', contexto)



def estacion_form(request):

    if request.method == "POST":
        mi_formulario = Estac_Form(request.POST)

        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data

            estacionar = Estacionamiento(PrecioHora=data.get('PrecioHora'), hora_ingreso=data.get('hora_ingreso'), hora_egreso=data.get('hora_egreso'))
            
            estacionar.save()

            return redirect('AppEstacionamiento')
        
    contexto = {
        'form': Estac_Form()
    }

    return render(request,"Apps/estacion_form.html", contexto)



def estacionamiento(request):
    estacionamientos = Estacionamiento.objects.all()
            
    contexto = {
        'estacionamientos': estacionamientos
    }

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


