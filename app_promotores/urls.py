from django.urls import path, include
from app_promotores import views

urlpatterns = [
    path('', views.promotores_listado, name='promotores_listado'),
    path('emprendimiento_nuevo/', views.emprendimiento_nuevo, name='emprendimiento_nuevo'),

]