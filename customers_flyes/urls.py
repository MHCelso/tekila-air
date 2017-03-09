from django.conf.urls import url, include
from rest_framework import routers
from .views import CustomerViewSet
from .views import FlyViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'flyes', FlyViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]