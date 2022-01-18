from django.db import models
# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Posteador(models.Model):
    nombre = models.CharField(max_length=255)           # Nombre de usuario
    create_at = models.DateTimeField(auto_now_add=True) # Fecha de registro
    ## Designa que administrador creo dicho elemento Usuario
    create_by = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE) 

    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
