from django.shortcuts import render, redirect
from .models import Parroquia, Barrio, PresidenteBarrio
from .forms import ParroquiaForm, BarrioForm

def index(request):
    parroquias = Parroquia.objects.all()
    barrios = Barrio.objects.all()
    presidentes = PresidenteBarrio.objects.all()
    informacion_template = {
        'parroquias': parroquias,
        'numero_parroquias': len(parroquias),
        'barrios': barrios,
        'presidentes': presidentes
    }
    return render(request, 'index.html', informacion_template)

def crear_parroquia(request):
    """ """
    print(request)
    if request.method == "POST":
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {"formulario": formulario}

    return render(request, "crear_parroquia.html", diccionario)

def editar_parroquia(request, id):
    """ """
    print("---------------")
    print(request)
    print("---------------")
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == "POST":
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {"formulario": formulario}

    return render(request, "editar_parroquia.html", diccionario)

def crear_barrio(request):
    """ """
    print(request)
    if request.method == "POST":
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {"formulario": formulario}

    return render(request, "crear_barrio.html", diccionario)

def editar_barrio(request, id):
    """ """
    print("---------------")
    print(request)
    print("---------------")
    barrio = Barrio.objects.get(pk=id)
    if request.method == "POST":
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {"formulario": formulario}

    return render(request, "editar_barrio.html", diccionario)
