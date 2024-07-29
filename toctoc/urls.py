"""
URL configuration for toctoc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  include, path
from toc_toc.views import index, solo_arrendadores, solo_arrendatarios, profile, edit_user, change_password
from inmuebles.views import nuevo_inmueble, crear_inmueble, editar_inmueble, eliminar_inmueble, detalle_inmueble

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('accounts/profile/', profile, name='profile'),
    path('edit-user/', edit_user, name='edith_user'),
    path('accounts/change-pass/', change_password, name='change_password'),
    path('inmuebles/nuevo/', nuevo_inmueble, name='nuevo_inmueble'),
    path('inmuebles/crear/', crear_inmueble, name='crear_inmueble'),
    path('inmuebles/editar/<id>/', editar_inmueble, name='editar_inmueble'),
    path('eliminar/inmueble/<id>/', eliminar_inmueble,name="eliminar_inmueble"),
    path('detalle/inmueble/<id>/', detalle_inmueble, name='detalle_inmueble'),
   
]