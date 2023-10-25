# Generated by Django 4.2.2 on 2023-06-26 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_general', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True, verbose_name='Zona')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Promotor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=35, verbose_name='Apellidos')),
                ('nombre', models.CharField(max_length=35, verbose_name='Nombres')),
                ('cuil', models.CharField(help_text='Sin guiones', max_length=11, unique=True, verbose_name='CUIL')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('email', models.EmailField(help_text='Correo Electrónico', max_length=254, unique=True)),
                ('domicilio', models.CharField(max_length=80)),
                ('cp', models.CharField(help_text='Ejemplo 4700', max_length=10, verbose_name='Código Postal')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('dpto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_general.departamento', verbose_name='Departamento')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_general.municipio')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_general.provincia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_promotores.zona')),
            ],
            options={
                'verbose_name': 'Promotor',
                'verbose_name_plural': 'Promotores',
                'ordering': ['apellido', 'nombre'],
            },
        ),
    ]
