from django.contrib import admin
from .models import *

# Registramos todos los modelos en el panel de administración

admin.site.register(Proyecto) 
admin.site.register(Ejemplo)