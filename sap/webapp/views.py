from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido(request):
    #return HttpResponse('Hola mundo desde Django')
    no_personas = Persona.objects.count()
    #personas= Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas})

def domicilioper(request):
    nomber_personas_domicilio = Domicilio.objects.count()
    personas_domici = Domicilio.objects.all()
    return render(request, 'domicilioper.html', {'nomber_personas_domicilio': nomber_personas_domicilio, 'personas_domici': personas_domici})





