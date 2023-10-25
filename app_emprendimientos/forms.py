from django import forms
from django.forms import DateInput, ModelForm
from app_emprendimientos.models import Emprendimiento


class FormEmprendimiento(ModelForm):
    class Meta:
        model = Emprendimiento
        fields = ['nombre', 'inicio', 'descripcion', 'telefono', 'celular', 'domicilio', 'provincia', 'dpto', 'municipio', 'cp', 'referente', 'promotor']
        