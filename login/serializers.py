from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
	"""
	Clase que serializa lo datos del modelo User
	para la creacion del formulario
	"""
	class Meta:
		model = User
		fields = ('username', 'email', 'password')