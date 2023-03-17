from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
###from .models import alumno, materia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import productos


# Create your views here.

def saludo(request):
    return HttpResponse("Welcome to my site")

"""def alumno_table(request):
    capturar = list(alumno.objects.values())
    return JsonResponse(capturar, safe= False)

def materia_table(request):
    capturar = list(materia.objects.values())
    return JsonResponse(capturar, safe=False)"""

def index(request):
  return render(request, "index.html")

def pant_mujer (request):
    return render(request, "pantalones-mujeres.html")

def blusas(request):
    return render(request, "blusas.html")

def zap_dama(request):
    return render(request, "zapatos-dama.html")

def login_page(request):
    return render(request, "login.html")

def contactanos(request):
    return render(request, "formulario_mardon.html")

def reset(request):
    return render(request, "resetpassword.html")

def form(request):
    if request.method == "GET":
        return render(request, 'signup.html', 
      {
        'form': UserCreationForm

      })   
    else:
        if request.POST['password1'] == request.POST['password2']:
    #Registrar usuario
    #Validacion de datos capturados, y evitar errores en la app y base de datos, se crea un objeto de acuerdo a lo que el usuario digite.
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1']) 
                user.save()
                return render(request, "signup.html", {   ##orden >> request > hacia donde >> diccionario de datos {}
                    'form': UserCreationForm,
                    "error":'Creado satisfactoriamente'
                
                })
                ###login(request, user)
                ###return redirect('home') ##Cuando el usuario se registre, este retornara a la pagina del proyecto central, por ejemplo "home"
            except:
                return render(request, "signup.html", {   ##orden >> request > hacia donde >> diccionario de datos {}
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'

                }
                              
                              )
    return render(request, "signup.html", {   ##orden >> request > hacia donde >> diccionario de datos {}
                    'form': UserCreationForm,
                    "error": 'El password no coincide'

                }
                              
                              )


def producto(request):
    t = productos.objects.filter(id="1")
    return render(request, 'db.html', {

        't': t

    })

def cafe(request):
    t = productos.objects.filter(id="2")
    return render(request, 'pant-cafe.html', {

        't': t

    })


