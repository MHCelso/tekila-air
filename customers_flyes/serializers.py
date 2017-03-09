from .models import Customer
from .models import Fly
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'

class FlySerializer(serializers.ModelSerializer):
	alias_from_customers = serializers.StringRelatedField(many=False)
	class Meta:
		model = Fly
		fields = ('reservation_id', 'fly_number', 'fly_date', 'seat_number', 'rute', 'alias_from_customers')


	