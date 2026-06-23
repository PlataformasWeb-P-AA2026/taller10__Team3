from django.shortcuts import render
from .models import *

def index(request):
    parroquias = Parroquia.objects.all()
    barrios = Barrio.objects.all()
    presidentes = PresidenteBarrio.objects.all()
    informacion_template = {
        'parroquias': parroquias,
        'barrios': barrios,
        'presidentes': presidentes
    }
    return render(request, 'index.html', informacion_template)