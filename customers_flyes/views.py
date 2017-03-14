from rest_framework import viewsets
from .models import Customer
from .models import Fly
from .serializers import CustomerSerializer
from .serializers import FlySerializer


class CustomerViewSet(viewsets.ModelViewSet):
	"""
	Clase que maneja los datos del Cliente a ser mostrados en la api
	"""
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


class FlyViewSet(viewsets.ModelViewSet):
	"""
	Clase que maneja los datos de Vuelos a ser mostrados en la api
	"""
	queryset = Fly.objects.all()
	serializer_class = FlySerializer