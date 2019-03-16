from django.db import models
from django.contrib.auth.models import User

class UsersMetadata(models.Model):

    id = models.AutoField('Id', primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fk_user_metadata_user')
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)
    direccion = models.CharField(max_length=3)
    telefono = models.CharField(max_length=20)
    fecha = models.DateField(auto_now=True)
    
    def __str__(self):
            return self.nombre