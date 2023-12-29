from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Persona
# Create your views here.
def home(request):
	personasListadas = Persona.objects.all()
	return render(request, "gestionPersonas.html", {"personas": personasListadas})

def registrarPersona(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        edad = request.POST['numEdad']
        salario = request.POST['numSalario']

        per = Persona.objects.create(nombre=nombre, edad=edad, salario=salario)
        return redirect('/')

def eliminar_Persona(request, id):
	per = Persona.objects.get(id=id)
	per.delete()
	return redirect('/')

def edicion(request, id):
	per = Persona.objects.get(id=id)
	return render(request, "editar.html", {"persona": per})

def editar_persona(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        nombre = request.POST['txtNombre']
        edad = int(request.POST['numEdad'])
        salario = float(request.POST['numSalario'])

        persona = Persona.objects.get(id=id)
        persona.nombre = nombre
        persona.edad = edad
        persona.salario = salario
        persona.save()
        return redirect('/')
