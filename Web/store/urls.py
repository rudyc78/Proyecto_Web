from django.urls import path
from . import views

urlpatterns = [

path('',views.index),
path('pant_mujer/', views.pant_mujer),
path('blusas/', views.blusas),
path('index/', views.index),
path('album/', views.album),


]