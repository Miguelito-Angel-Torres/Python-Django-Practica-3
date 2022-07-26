from django.shortcuts import render,redirect
#Importar en models la clase Curso de

from .models import Curso

# Create your views here.
# Importacion para enviar mensajes
from django.contrib import messages

def home(request):
    cursosx= Curso.objects.all()
    messages.success(request,'!Cursos listados!')

    return render(request, 'gestionCursos.html',{'cursos':cursosx})


def registrarCurso(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    credito = request.POST["txtCreditos"]

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=credito)
    
    messages.success(request,'!Cursos registrado!')
    return redirect('/')

    # Se va al mismo html

def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request,'!Cursos eliminado')
    return redirect('/')

def edicionCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'edicionCurso.html',{"curso":curso})



def editarCurso(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    credito = request.POST["txtCreditos"]

    curso = Curso.objects.get(codigo=codigo)

    curso.nombre = nombre
    curso.creditos = credito
    # metodos para guardar los datos del cursos --cambios
    curso.save()

    messages.success(request,'!Cursos actualizado')

    return redirect('/')

