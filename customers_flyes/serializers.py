"""
Serializadores para ser utilizados en la api creada con Djangorestframework.
"""
# importacion del modelo User de Django
from .models import Customer
# importacion del modelo fly creado
from .models import Fly
# importacion del objeto serializers
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
	"""
	Clase que hara el serializado del modelo Customer
	"""
	# Clase Meta
	class Meta:
		# variable que almacena el modelo Customer
		model = Customer
		# variable que contiene los campos a ser serializados
		fields = '__all__'

class FlySerializer(serializers.ModelSerializer):
	"""
	Clase que serializara los campos del modelo Fly
	"""
	alias_from_customers = serializers.StringRelatedField(many=False)
	# Clase Meta
	class Meta:
		# variable que contiene el modelo Fly
		model = Fly
		# variable que contiene los campos a ser serializados
		fields = ('reservation_id', 'fly_number', 'fly_date', 'seat_number', 'rute', 'alias_from_customers')


	