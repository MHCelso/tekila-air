from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
	alias = models.CharField('Alias', max_length=50)
	name = models.CharField('Nombre(s)', max_length=50)
	last_name = models.CharField('Apellido(s)', max_length=50)
	phone_number = models.CharField('Telefono', max_length=50)
	SEX = (('M', 'Masculino'), ('F', 'Femenino'))
	gender = models.CharField('Genero', max_length=1, choices=SEX)
	birth_date = models.DateField('Fecha de nacimiento', auto_now_add=False)
	def __unicode__(self):
		return self.name


class Fly(models.Model):
	reservation_id = models.IntegerField('Id de reserva', null=False)
	fly_number = models.IntegerField('Numero de vuelo', null=False)
	fly_date = models.DateTimeField('Fecha del Vuelo', auto_now_add=False)
	seat_number = models.IntegerField('Numero de asiento', null=False)
	rute = models.CharField('Ruta', max_length=50)
	customer_alias = models.ForeignKey(Customer, related_name='alias', on_update=models.CASCADE)
	def __unicode_(self):
		return self.fly_number

 