from django.shortcuts import render

# Create your views here.
from app_promotores.models import Promotor


def promotores_listado(request):
    promotores = Promotor.objects.all()
    return render(request, "app_promotores/promotores_listado.html", {'promotores':promotores})


def emprendimiento_nuevo(request):
    return render(request, "app_promotores/emprendimiento_nuevo.html", {})

