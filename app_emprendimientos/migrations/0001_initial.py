# Generated by Django 4.2.2 on 2023-06-26 11:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_general', '0001_initial'),
        ('app_promotores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprendimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Emprendimiento')),
                ('inicio', models.DateField(verbose_name='Inicio Actividad')),
                ('descripcion', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('telefono', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=80)),
                ('cp', models.CharField(help_text='Ejemplo 4700', max_length=10, verbose_name='Código Postal')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('dpto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_general.departamento', verbose_name='Departamento')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_general.municipio')),
                ('promotor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_promotores.promotor')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_general.provincia')),
                ('referente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_general.persona')),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Emprendimiento',
                'verbose_name_plural': 'Emprendimientos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Emprendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('emprendimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_emprendimientos.emprendimiento')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_general.persona')),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Emprendedor',
                'verbose_name_plural': 'Emprendedores',
                'ordering': ['-created'],
            },
        ),
    ]
