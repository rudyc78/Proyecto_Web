from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class productos(models.Model):
    marca = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()

    def __str__(self):
        return  self.marca
    
    

