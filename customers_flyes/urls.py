from django.conf.urls import url, include
from rest_framework import routers
from .views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]