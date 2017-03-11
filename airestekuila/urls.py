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
from django.conf.urls import url, include
from django.contrib import admin
from login.views import IndexView
from login.views import LoginView
from login.views import user_login
from login.views import user_logout
from login.views import CustomerRegister
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

    

urlpatterns = [
    url(r'^get-token/', obtain_jwt_token),
    url(r'^verify-token/', verify_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-users/', include('login.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='base'),
    # url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^registrar-usuarios/$', CustomerRegister.as_view(), name='registrar-usuarios'),
    url(r'^api/', include('customers_flyes.urls')),
]