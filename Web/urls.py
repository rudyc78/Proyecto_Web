"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ="home"),
    path('pant_mujer/', views.pant_mujer, name = 'pant-mujer'),
    path('blusas/', views.blusas, name = "blusas"),
    path('zap-damas/', views.zap_dama, name ="zapdamas"),
    path('login/', views.login_page, name ='login'),
    path('contactanos/', views.contactanos, name ='contactanos'),
    path('signup/', views.form, name="signup"),
    path('reset/', views.reset, name='reset'),
    path('db/', views.producto, name='db'),
    path('cafe/', views.cafe, name='cafe'),
    


   


]
