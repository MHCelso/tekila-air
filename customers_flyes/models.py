from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
	"""
	Clase que crea el modelo Customer (cliente), el modelo servira para gusradar los clientes registrados.
	"""
	# variable campo que hace la recion uno a uno del modelo cliente con el modelo User de Django. 
	user = models.OneToOneField(User)
	# variable campo de tipo character para el almacenado del alias del cliente
	alias = models.CharField('Alias', max_length=50)
	# variable campo de tipo character para el almacenado del nombre del cliente
	name = models.CharField('Nombre(s)', max_length=50)
	# variable campo de tipo character para el almacenado de los apellidos del cliente
	last_name = models.CharField('Apellido(s)', max_length=50)
	# variable campo de tipo character para el almacenado del telefono del cliente
	phone_number = models.CharField('Telefono', max_length=50)
	# variable que lamacena una tupla con dis tuplas que contienen generos para el cliente registrado
	SEX = (('M', 'Masculino'), ('F', 'Femenino'))
	# variable campo de tipo character para el almacenado del genero del cliente la cual consta de dos opciones 'Masculino' y 'Femenino'
	gender = models.CharField('Genero', max_length=1, choices=SEX)
	# variable campo de tipo DateField para el almacenado de la fecha de nacimiento del cliente
	birth_date = models.DateField('Fecha de nacimiento', auto_now_add=False, null=True)
	def __unicode__(self):
		"""
		Funcion unicode que retorna el valor de alguno de los campos del cliente
		esto se ve representado en el administrador de Django
		"""
		# retorno del valor de alias para ser mostrado en el administrador de Django
		return self.alias


class Fly(models.Model):
	"""
	Clase crea el modelo Fly (vuelo) para registrar vuelos agendados por cliente
	o por el super usuario del sitio o administrador.
	"""
	# variable campo de tipo integer para el almacenado del id de reservacion del vuelo del cliente
	reservation_id = models.IntegerField('Id de reserva', null=False)
	# variable campo de tipo integer para el almacenado del numero de vuelo del cliente
	fly_number = models.IntegerField('Numero de vuelo', null=False)
	# variable campo de tipo DateTimeField para el guardado de la fecha y hora del vuelo
	fly_date = models.DateTimeField('Fecha del Vuelo', auto_now_add=False)
	# variable campo de tipo integer para el almacenado del numero del asiento de avion
	seat_number = models.IntegerField('Numero de asiento', null=False)
	# variable campo de tipo Character para el almacenamiento de la ruta del vuelo
	rute = models.CharField('Ruta', max_length=50)
	# variable campo de tipo foranea que conecta al modelo Customer
	alias_from_customers = models.ForeignKey(Customer, null=False, default='')
	def __unicode__(self):
		"""
		funcion unicode que retorna el valor de la variable ruta para ser mostrada en 
		el administrador de Django.
		"""
		# retorno del valor de la ruta
		return self.rute