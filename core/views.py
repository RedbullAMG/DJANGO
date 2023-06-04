from django.shortcuts import render, redirect
from .models import Vehiculo
from .form import VehiculosForm

# Create your views here.
def home(request):

    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos':vehiculos
    }

    return render (request,'core/home.html', datos)

def Pagina2(request):
    
    datos = {
        'form':VehiculosForm()
    }
    if request.method=='POST':
        formulario= VehiculosForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    
    return render (request,'core/pagina2.html', datos)

def mod_vehiculo(request, id):
    auto = Vehiculo.objects.get(patente=id)
    datos = {
        'form':VehiculosForm()
    }
    if request.method=='POST':
        formulario= VehiculosForm(data=request.POST, intance=auto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados Correctamente"
        return render (request,'core/mod_vehiculo.html', datos)
    

def listar_mod_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos':vehiculos
    }

    return render (request,'core/listar_mod_vehiculo.html', datos)
    
