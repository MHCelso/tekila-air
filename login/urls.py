from django.conf.urls import url, include
# from django.contrib.auth.decorators import login_required
from .views import LoginView
from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
]