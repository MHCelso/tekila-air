from django.contrib import admin
from .models import Customer
from .models import Fly

"""
Se registraron los modelos Customer y Fly al administrador de Django
"""
# registro de Customer al administrador
admin.site.register(Customer)
# Registro de Fly al administrador
admin.site.register(Fly)