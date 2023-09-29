from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Ejemplo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    contenido_xml = models.TextField()  # Aquí puedes almacenar el contenido XML del ejemplo

    def __str__(self):
        return self.nombre
