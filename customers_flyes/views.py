from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .models import Fly
from .serializers import CustomerSerializer
from .serializers import FlySerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


class FlyViewSet(viewsets.ModelViewSet):
	queryset = Fly.objects.all()
	serializer_class = FlySerializer