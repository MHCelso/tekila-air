# from django.shortcuts import render
# from django.views import View
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views.generic import TemplateView
from .serializers import UserSerializer

# class IndexView(View):
#	def get(self, request, *args, **kwargs):
#		return render(request, 'base.

class IndexView(TemplateView):
    template_name = "base.html"


class LoginView(TemplateView):
    template_name = "login_form.html"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer