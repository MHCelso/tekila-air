"""
Modulo en el cual se pondran las urls a ser servidas por el router
que ofrece DjangoRestFramework
"""
# obetos de Django para incluir urls
from django.conf.urls import url, include
# importacion del router de DjangoRestframework
from rest_framework import routers
# importacion de la vista que manejara el modelo Clientes
from .views import CustomerViewSet
# importacion de la vista que manejara los vuelos
from .views import FlyViewSet
# variable que guradara el ruteo de la surls de la api
router = routers.DefaultRouter()
# agregado de la url que contiene la view del modelo cliente
router.register(r'customers', CustomerViewSet)
# agregado de la url que contiene la view del Modelo vuelo
router.register(r'flyes', FlyViewSet)
# Lista inclusion del router con las url's registradas 
urlpatterns = [
# inclusion del router con las url's registradas
	url(r'^', include(router.urls)),
]