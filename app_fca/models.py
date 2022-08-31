from email.policy import default
from django.db import models

# Create your models here. Class CamelCase 

class Docentes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    titulo_grado=models.CharField(max_length=40)
    titulo_posgrado=models.CharField(max_length=40)
    hs_asignar=models.IntegerField()
    metodo_alta=models.CharField(max_length=100)
    fecha_alta=models.DateField()