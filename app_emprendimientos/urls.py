from django import views
from django.urls import path, include
from app_emprendimientos import views


urlpatterns = [
    path('', views.emprendimientos, name='emprendimientos'),
    path('emprendimiento_nuevo/', views.emprendimiento_nuevo, name='emprendimiento_nuevo'),
    path('emprendimiento_editar/<int:id>', views.emprendimiento_editar, name='emprendimiento_editar'),
          
]