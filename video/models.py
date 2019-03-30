from django.db import models

# Create your models here.
class Video(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    slug = models.SlugField(max_length=50)
    fecha = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.titulo

    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Video'    