from django.contrib.auth.models import User
from customers_flyes.models import Customer
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
	"""
	Calse que majena la creacion de forularios usando
	formularios que Dajngo nos ofrece
	"""
	alias = forms.CharField()
	nombre = forms.CharField()
	apellidos = forms.CharField()
	telefono = forms.CharField()
	genero = forms.CharField()
	fecha_de_nacimiento = forms.DateField()
