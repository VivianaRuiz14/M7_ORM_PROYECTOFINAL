from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from toc_toc.models import Inmueble, Region, Comuna
from toc_toc.services import crear_inmueble as crear_inmueble_service, eliminar_inmueble as eliminar_inmueble_service
from inmuebles.forms import InmuebleForm

# vamos a crear un test que sólo pasan los 'arrendadores'
def solo_arrendadores(user):
  if user.user_profile.rol == 'arrendador' or user.is_staff == True:
    return True
  else:
    return False
  
@user_passes_test(solo_arrendadores)
def editar_inmueble(req, id):
  if req.method == 'GET':
    # 1. Se obtiene el inmueble para editar
    inmueble = Inmueble.objects.get(id=id)
    # 2. Se obtiene las regiones y las comunas
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    # 3.Se obtiene el código de la region
    # cod_region = inmueble.comuna.region.cod
    cod_region_actual = inmueble.comuna_id[0:2]
    # 4. Creo el 'context' con toda la info que requiere
    context = {
      'inmueble': inmueble,
      'regiones': regiones,
      'comunas': comunas,
      'cod_region': cod_region_actual
    }
    return render(req, 'editar_inmueble.html', context)
  else:
    return HttpResponse('Se realizaron modificaciones de manera exitosa')


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
def eliminar_inmueble(req, id):
  eliminar_inmueble_service(id)
  messages.error(req, 'Inmueble ha sido eliminado')
  return redirect('/accounts/profile/')


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
  messages.success(req, 'Propiedad Creada')
  return redirect('/accounts/profile/')


  
@login_required
def detalle_inmueble(req, id):
    id=int(id)
    inmueble = Inmueble.objects.get(id=id)
    
    context ={
        'inmueble':inmueble
    }
    return render(req, 'detalle_inmueble.html', context)
