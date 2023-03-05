from django.urls import path
from . import views

urlpatterns = [

path('',views.album),
path('alumno/', views.alumno_table),
path('materia/', views.materia_table),
path('index/', views.index),
path('album', views.album),

]