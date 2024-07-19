from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from toc_toc.services import editar_user_sin_password, change_password

# Create your views here.
@login_required
def home(request):
  return render(request, 'home.html')

@login_required
def profile(request):
  return render(request, 'profile.html')

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
      req.POST['telefono'])
  else:
    editar_user_sin_password(
      current_user.username,
      req.POST['first_name'],
      req.POST['last_name'],
      req.POST['email'],
      req.POST['direccion'])
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