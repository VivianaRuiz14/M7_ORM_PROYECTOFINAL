# Generated by Django 5.0.6 on 2024-07-10 23:46

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('cod', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('cod', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=1500)),
                ('m2_construidos', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('m2_totales', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cant_estacionamientos', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cant_habitaciones', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('cant_baños', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('direccion', models.CharField(max_length=255)),
                ('tipo_inmueble', models.CharField(choices=[('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega')], max_length=255)),
                ('precio_mensual', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000)])),
                ('precio_ufs', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='inmueble', to='toc_toc.comuna')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='inmuebles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='comunas', to='toc_toc.region'),
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada')], max_length=50)),
                ('Inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='toc_toc.inmueble')),
                ('arrendador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
