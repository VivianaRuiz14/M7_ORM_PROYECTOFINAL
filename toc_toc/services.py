from django.contrib.auth.models import User
from toc_toc.models import UserProfile
from django.db.utils import IntegrityError

def crear_inmueble(*args):
    pass

def editar_inmueble(*args):
    pass

def eliminar_inmueble(*args):
    pass

def crear_user(username, first_name, last_name, email, password, pass_confirm, direccion, telefono=None) -> list[bool,str]:
    # validacion que las password coincidan
    if password != pass_confirm:
        return False, 'Las contraseñas no coinciden'
    # creamos el objeto user
    try:
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
    except IntegrityError:
        # se le da feedback al usuario
        return False, 'Rut duplicado'
    # Creamos el UserProfile
    UserProfile.objects.create(user=user, direccion=direccion, telefono=telefono)
    # Si todo sale bien retornamos True
    return True, None

def editar_user(username, first_name, last_name, email, password, direccion, telefono=None) -> list[bool,str]:
    # Nos traemos el Username y lo modificamos
    user = User.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password = (password)
    user.save()
    # Nos traemos el userprofile y modificamos sus datos
    user_profile = UserProfile.objects.get(user=user)
    user_profile.direccion = direccion
    user_profile.telefono = telefono
    user_profile.save()
    
    def eliminar_user(user_id):
        pass
    
