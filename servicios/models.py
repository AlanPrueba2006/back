from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='servicios/', default='servicios/default.jpg')

    def __str__(self):
        return self.titulo
