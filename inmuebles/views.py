from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from toc_toc.models import Inmueble, Region, Comuna
from toc_toc.services import crear_inmueble as crear_inmueble_service

# vamos a crear un test que sólo pasan los 'arrendadores'
def solo_arrendadores(user):
  if user.user_profile.rol == 'arrendador' or user.is_staff == True:
    return True
  else:
    return False

@user_passes_test(solo_arrendadores)
def nuevo_inmueble(req):
  # nos traemos la información de las comunas y las regiones
  regiones = Region.objects.all()
  comunas = Comuna.objects.all()
  # pasar los datos requeridos por el formulario
  context = {
    'tipos_inmueble': Inmueble.tipos,
    'regiones': regiones,
    'comunas': comunas
  }
  return render(req, 'nuevo_inmueble.html', context)

@user_passes_test(solo_arrendadores)
def crear_inmueble(req):
  # obtener el rut del usuario
  propietario_rut = req.user.username
  # validar metraje (construídos vs totales)
  crear_inmueble_service(
    req.POST['nombre'],
    req.POST['descripcion'],
    int(req.POST['m2_construidos']),
    int(req.POST['m2_totales']),
    int(req.POST['num_estacionamientos']),
    int(req.POST['num_habitaciones']),
    int(req.POST['num_baños']),
    req.POST['direccion'],
    req.POST['tipo_inmueble'],
    int(req.POST['precio']),
    req.POST['comuna_cod'],
    propietario_rut
  )
  return HttpResponse('llegamos!')