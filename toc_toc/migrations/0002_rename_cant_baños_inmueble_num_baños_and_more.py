# Generated by Django 5.0.6 on 2024-07-12 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toc_toc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='cant_baños',
            new_name='num_baños',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='cant_estacionamientos',
            new_name='num_estacionamientos',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='cant_habitaciones',
            new_name='num_habitaciones',
        ),
    ]
