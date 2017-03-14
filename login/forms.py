from django.contrib.auth.models import User
from customers_flyes.models import Customer
from django import forms
from django.contrib.auth.forms import UserCreationForm

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ('alias', 'name', 'last_name', 'phone_number', 'gender', 'birth_date')

class UserForm(UserCreationForm):
	alias = forms.CharField()
	nombre = forms.CharField()
	apellidos = forms.CharField()
	telefono = forms.CharField()
	genero = forms.CharField()
	fecha_de_nacimiento = forms.DateField()
