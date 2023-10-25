from django.urls import path
from app_general import views



urlpatterns = [
    path('', views.index, name='index'), 
    path('register/', views.register, name='register'),  
    path('autoridades/', views.autoridades, name='autoridades'),
    
    path('password_reset_request/', views.password_reset_request, name='password_reset_request'),
    path('detalle_profile/<int:id>', views.detalle_profile, name = 'detalle_profile'),
    path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    
]

