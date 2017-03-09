from .models import Customer
from .models import Fly
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'

class FlySerializer(serializers.ModelSerializer):
	alias = serializers.StringRelatedField(many=True)
	class Meta:
		model = Fly
		fields = '__all__'