from django.shortcuts import render

# Create your views here.
from web.models import Tarifas


def Home(request):


    return render(request,'index.html')

def Tarifa(request):
    #usando el modelo para traer datos de bd
    tarifas = Tarifas.objects.all()

    #crear un diccionario con los datos a enviar
    diccionario={
        'tarifas':tarifas
    }
    return render(request,'tarifas.html',diccionario) 