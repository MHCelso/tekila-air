from django.shortcuts import render
from django.contrib.auth.models import User
from customers_flyes.models import Customer
from customers_flyes.models import Fly
from rest_framework import viewsets
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import TemplateView, FormView
from django.views import View
from .serializers import UserSerializer
from .forms import UserForm

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
			return HttpResponse('Datos incorrectos')
	else:
		return render(request, 'login_form.html', {}, context)


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


class CustomerRegister(FormView):
	template_name = "register.html"
	form_class = UserForm
	success_url = '/'

	def form_valid(self, form):
		user = form.save()
		customer = Customer()
		customer.user = user
		customer.alias = form.cleaned_data['alias']
		customer.name = form.cleaned_data['nombre']
		customer.last_name = form.cleaned_data['apellidos']
		customer.phone_number = form.cleaned_data['telefono']
		customer.gender = form.cleaned_data['genero']
		customer.birth_date = form.cleaned_data['fecha_de_naciemiento']
		customer.save()
		return super(CustomerRegister, self).form_valid(form)


class FlightsRegister(TemplateView):
	template_name = "register_flight.html"

	def post(self, request, *args, **kwargs):
		fly = Fly()
		if request.method == "POST":
			fly.reservation_id = request.POST.get("reservation-id")
			fly.fly_number = request.POST.get("fly-number")
			fly.fly_date = request.POST.get("fly-date")
			fly.seat_number = request.POST.get("seat-number")
			fly.rute = request.POST.get("rute")
			fly.alias_from_customers_id = request.POST.get("customer-alias")
			fly.save()

			return render(request, self.template_name, {})
		return render(request, self.template_name, {})



class GetCustomers(TemplateView):
	template_name = "see_customers.html"

	def post(self, request, *args, **kwargs):
		customer = Customer
		if request.method == "POST":
			clientes = customer.objects.all()

			return render(request, self.template_name, {'clientes': clientes, 'cliente': True})
		return render(request, self.template_name, {})