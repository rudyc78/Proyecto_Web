from django.urls import path
from . import views

urlpatterns = [

path('',views.saludo),
path('alumno/', views.alumno_table),
path('materia/', views.materia_table)

]