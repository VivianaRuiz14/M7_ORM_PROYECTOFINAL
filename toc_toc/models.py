from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True)
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=255)
         
class Inmueble(models.Model):
        
    tipos = (('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega'))
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1500)
    m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales = models.IntegerField(validators=[MinValueValidator(1)])
    cant_estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    cant_habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    cant_baños = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    direccion = models.CharField(max_length=255)
    tipo_inmueble = models.CharField(max_length=255, choices=tipos)
    precio_mensual = models.IntegerField(validators=[MinValueValidator(1000)], null=True)
    precio_ufs = models.FloatField(validators=[MinValueValidator(1.0)], null=True)
    # llaves foraneas
    comuna = models.ForeignKey(Comuna, related_name='inmueble', on_delete=models.RESTRICT)
    propietario = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='inmuebles')
      
class Solicitud(models.Model):
    estados = (('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada'))
    Inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
    arrendador = models.ForeignKey(User, related_name='solicitudes', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=estados)
    
          
          