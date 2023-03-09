from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import alumno, materia


# Create your views here.

def saludo(request):
    return HttpResponse("Welcome to my site")

def alumno_table(request):
    capturar = list(alumno.objects.values())
    return JsonResponse(capturar, safe= False)

def materia_table(request):
    capturar = list(materia.objects.values())
    return JsonResponse(capturar, safe=False)

def index(request):
  return render(request, "index.html")

def pant_mujer (request):
    return render(request, "blusas.html")

def cart(request):
    return render(request, "Shopping cart.html")

def album (request):
    return render(request, "Album.html")

