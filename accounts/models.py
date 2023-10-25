from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='user/', verbose_name='Imagen de Perfil')
    addres = models.CharField(max_length=150, null=True, blank=True, verbose_name='dirección')
    location = models.CharField(max_length=100, null=True, blank=True, verbose_name='Localidad')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username
    

# esto es para cuando creo un usiario tambien crea el perfil
def create_user_profile(sender, instance, created, **kwargs) :
    if created:
        Profile.objects.create(user=instance)

# funcion que cuando graba el perfil se graba en la BD
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# con estos eventos logro conectar el usuario con el perfil
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


