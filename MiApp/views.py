from django.shortcuts import redirect, render

from MiApp.forms import Estac_Form

from .models import Entrada, Estacionamiento, Salida


def estacion_form(request):

    if request.method == "POST":
        mi_formulario = Estac_Form(request.POST)

        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data

            estacionar = Estacionamiento(PrecioHora=data.get('PrecioHora'), hora_ingreso=data.get('hora_ingreso'), hora_egreso=data.get('hora_egreso'))
            
            estacionar.save()

            return redirect('AppEstacionamientoForm')

    estacionamientos = Estacionamiento.objects.all()
            
    contexto = {
        'form': Estac_Form(),
        'estacionamientos': estacionamientos
    }

    return render(request,"Apps/estacion_form.html", contexto)



def estacionamiento(request):
    estacionar = Estacionamiento(PrecioHora="400", hora_ingreso="2022-09-06 15:00:00", hora_egreso= "2022-09-06 16:00:00")
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


