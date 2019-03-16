from django.db import models

class Productos(models.Model):

    id = models.AutoField('Id', primary_key=True)
    url = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    epigrafe = models.CharField(max_length=100)
    fecha = models.DateField(auto_now=True)
    
    def __str__(self):
            return self.titulo