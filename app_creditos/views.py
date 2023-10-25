from django.shortcuts import render, get_object_or_404, redirect

from app_creditos.models import Linea, Destino


def creditos(request):
    return render(request, "app_creditos/creditos.html")


def linea_detalle(request, id):
    linea = get_object_or_404(Linea, pk=id)
    return render(request, "app_creditos/linea_detalle.html", {'linea':linea})



