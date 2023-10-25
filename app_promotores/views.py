from django.shortcuts import render

from app_promotores.models import Promotor


# Create your views here.


def promotores_listado(request):
    promotores = Promotor.objects.all()
    return render(request, "app_promotores/promotores_listado.html", {'promotores':promotores})


def emprendimiento_nuevo(request):
    return render(request, "app_promotores/emprendimiento_nuevo.html", {})

