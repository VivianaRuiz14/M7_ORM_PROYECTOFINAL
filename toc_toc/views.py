from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from toc_toc.models import Comuna, Inmueble, Region
from toc_toc.services import editar_user_sin_password
from django.db. models import Q

# Create your views here.
@login_required
def index(req):
  datos = req.GET
  region_cod = datos.get('region_cod', '')
  comuna_cod = datos.get('comuna_cod', '')
  palabra = datos.get('palabra', '')
  print(region_cod, comuna_cod, palabra)
  inmuebles = filtrar_inmuebles(region_cod, comuna_cod, palabra)
  comunas = Comuna.objects.all()
  regiones = Region.objects.all()
  context = {
    'comunas': comunas,
    'regiones': regiones,
    'inmuebles' : inmuebles
  }
  return render(req, 'index.html', context)

def filtrar_inmuebles(region_cod, comuna_cod, palabra):
    filtro_palabra = None
    if palabra != '':
      filtro_palabra = Q(nombre__icontains=palabra) | Q (descripcion__icontains=palabra)
    
    filtro_ubicacion = None
    if comuna_cod != '':
      comuna = Comuna.objects.get(cod=comuna_cod)
      filtro_ubicacion = Q(Comuna=comuna)
    
    elif region_cod  != '':
      region = Region.objects.get(cod=region_cod)
      comunas_region = region.comuna.all()
      filtro_ubicacion = Q(comuna__in=comunas_region)
      
    if filtro_ubicacion is None and filtro_palabra is None:
      return Inmueble.objects.all()
    
    elif filtro_ubicacion is None and filtro_palabra is None:
      return Inmueble.objects.filter(filtro_ubicacion)
    
    elif filtro_ubicacion is None and filtro_palabra is not None:
      return Inmueble.objects.filter(filtro_palabra)
    
    elif filtro_ubicacion is not None and filtro_palabra is not None:
      return Inmueble.objects.filter(filtro_palabra & filtro_ubicacion)

  

@login_required
def profile(request):
  user = request.user
  inmuebles = Inmueble.objects.filter(propietario=user)
  context = {
    'mis_inmuebles': inmuebles
  }
  return render(request, 'profile.html', context)

@login_required
def edit_user(req):
  # 1. Obtengo el usuario actual
  current_user = req.user
  # llamo a la función para editar el usuario
  if req.POST['telefono'] != '':
    # trailing whitespaces .strip()
    editar_user_sin_password(
      current_user.username,
      req.POST['first_name'],
      req.POST['last_name'],
      req.POST['email'],
      req.POST['direccion'],
      req.POST['rol'],
      req.POST['telefono'])
  else:
    editar_user_sin_password(
      current_user.username,
      req.POST['first_name'],
      req.POST['last_name'],
      req.POST['email'],
      req.POST['direccion']),
    req.POST['rol'],
  messages.success(req, "Ha actualizado sus datos con éxito")
  return redirect('/')

def change_password (req):
  # 1. recibo los datos del formulario
  password = req.POST['password']
  password_repeat = req.POST['password_repeat']
  # 2. valido que ambas contraseñas coincidan
  if password != password_repeat:
    messages.error(req, 'Las contraseñas no coinciden')
    return redirect('/accounts/profile')
  # 3. actualizamos las contraseñas
  req.user.set_password(password)
  req.user.save()
  messages.success(req,'Contraseña Actualizada')
  return redirect('/accounts/profile')

# pendientes 
def solo_arrendadores(req):
  return HttpResponse('sólo arrendadores')

def solo_arrendatarios(req):
  return HttpResponse('sólo arrendatarios')