"""airestekuila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # librerias importadas para el manejo de urls
from django.contrib import admin # importacion del administrador de Django
from login.views import IndexView # importacion de la clase para pagina principal
from login.views import user_login # importacion de la funcion que hace el logueo
from login.views import erase_fly # importacion de la funcion que elimina un vuelo
from login.views import erase_customer # importacion de la funcion que elimina un cliente
from login.views import user_logout # importacion de la funcion que hace el cierre de sesion
from login.views import CustomerRegister # importacion de la clase que crea un registro de cliente
from login.views import GetCustomers # importacion de la clase que consigue los clientes
from login.views import FlightsRegister # importacion de la clase que registra un vuelo
from login.views import MyAllFlights # importacion de la clase que muestra todos los vuelos
from rest_framework_jwt.views import obtain_jwt_token # importacion de la funcion que genera un web token
from rest_framework_jwt.views import verify_jwt_token # importacion de la funcion que verifica un web token
from rest_framework_jwt.views import refresh_jwt_token # importacion de la funcion que refresca un web token

    
urlpatterns = [
    # url para generar un web token
    url(r'^get-token/', obtain_jwt_token),
    # url para verificar un web token
    url(r'^verify-token/', verify_jwt_token), 
    # url para refrescar un web token
    url(r'^refresh-token/', refresh_jwt_token), 
    # url's que estan incluidas en la aplicacion login 
    url(r'^api-users/', include('login.urls')),
    # url que direcciona al administrador de Django 
    url(r'^admin/', admin.site.urls),
    # url que direcciona a la vista principal del sitio 
    url(r'^$', IndexView.as_view(), name='base'),
    # url que direcciona a la vista login del sitio
    url(r'^login/$', user_login, name='login'),
    # url que direcciona a la vista para borrar un vuelo
    url(r'^borrar-vuelo/$', erase_fly, name='borrar-vuelo'),
    # url que direcciona a la funcion que borra un cliente
    url(r'^borrar-cliente/$', erase_customer, name='borrar-cliente'),
    # url que hace el cierre de sesion
    url(r'^logout/$', user_logout, name='logout'),
    # url que direcciona a la vista para registrar usuarios
    url(r'^registrar-usuarios/$', CustomerRegister.as_view(), name='registrar-usuarios'),
    # url que direcciona a la vista para registrar vuelos
    url(r'^registrar-vuelos/$', FlightsRegister.as_view(), name='registrar-vuelos'),
    # url que direcciona a la vista para ver los vuelos registrados
    url(r'^ver-vuelos/$', MyAllFlights.as_view(), name='ver-vuelos'),
    # url que direcciona a la vista para ver clientes registrados
    url(r'^ver-clientes/$', GetCustomers.as_view(), name='ver-clientes'),
    # url para ir a la api creada con DjangorestFramework
    url(r'^api/', include('customers_flyes.urls')),
]