from django.shortcuts import render
# from django.views import View
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import TemplateView
from .serializers import UserSerializer

# class IndexView(View):
#	def get(self, request, *args, **kwargs):
#		return render(request, 'base.

def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Tu cuenta esta desactivada')
		else:
			# print("Inavlid Dates of the person {0}, {1}".format(username, password))
			return HttpResponse('Datos incorrectos')
	else:
		return render(request, 'login_form.html', {}, context)

@login_required
def restricted(request):
    return HttpResponse("Estas Logueado")


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


class IndexView(TemplateView):
    template_name = "base.html"


class LoginView(TemplateView):
    template_name = "login_form.html"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer