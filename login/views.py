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
	"""
	Funcion que realiza el login mediante el metodo post
	recibe dos variables y estas son validadas para poder acceder al sitio
	"""
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
def erase_fly(request):
	"""
	funcion que elimina un vuelo mediante una peticion post
	en ella se recibe el parametro a borrar (id)
	"""
	context = RequestContext(request)

	if request.method == "POST":
		id_flight = request.POST.get('erase-id')
		Fly.objects.filter(id=id_flight).delete()
		return HttpResponseRedirect('/')
	return render(request, 'my_flights.html', {}, context)


@login_required
def erase_customer(request):
	"""
	funcion que elimina un cliente registrado mediante una peticion post 
	recibe el parametro a borrar (id)
	"""
	context = RequestContext(request)

	if request.method == "POST":
		id_customer = request.POST.get('id-customer')
		Customer.objects.filter(id=id_customer).delete()
		return HttpResponseRedirect('/')
	return render(request, 'see_customers.html', {}, context)


@login_required
def user_logout(request):
	"""
	funcion que nos redirecciona al sierre de nuestro cierre de sesion.
	"""
    logout(request)
    return HttpResponseRedirect('/')


class IndexView(TemplateView):
	"""
	Clase que nos redirecciona a la vista principal del sitio.
	"""
    template_name = "base.html"


class UserViewSet(viewsets.ModelViewSet):
	"""
	Clase utilizada para la creacion de los formularios que registran un cliente.
	"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MyAllFlights(TemplateView):
	"""
	Clase que nos trae todos los vuelos utilizando el metodo GET para traer los vuelos 
	filtrados por cliente.
	Mediante el metodo post se traen todos los vuelos que seran vistos por el superusuario.
	"""
	template_name = 'my_flights.html'

	def post(self, request, *args, **kwargs):
		fly = Fly
		if request.method == "POST":
			allFlights = fly.objects.all()
			return render(request, self.template_name, {'flights': allFlights, 'flight': True})
		return render(request, self.template_name, {})

	def get(self, request, *args, **kwargs):
		fly = Fly
		if request.method == "GET":
			id = request.GET.get("id-flight")
			my_all_flights = fly.objects.filter(alias_from_customers_id=id)
			return render(request, self.template_name, {'flights': my_all_flights, 'flight': True})
		return render(request, self.template_name, {})

class CustomerRegister(FormView):
	"""
	Clase que es utilizada para la creacion de formularios en este caso para el formulario cliente.
	"""
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
		customer.birth_date = form.cleaned_data['fecha_de_nacimiento']
		customer.save()
		return super(CustomerRegister, self).form_valid(form)


class FlightsRegister(TemplateView):
	"""
	Clase utilizada para el registro de un vuelo.
	"""
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
	"""
	Clase utilizada para obtener todos los clientes.
	"""
	template_name = "see_customers.html"

	def post(self, request, *args, **kwargs):
		customer = Customer
		if request.method == "POST":
			clientes = customer.objects.all()

			return render(request, self.template_name, {'clientes': clientes, 'cliente': True})
		return render(request, self.template_name, {})