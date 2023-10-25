from django.urls import path, include
from app_creditos import views

urlpatterns = [
    path('', views.creditos, name='creditos'),
    # path('contacto/', views.creditos, name='contacto'),

]