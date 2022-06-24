from django.db import models
from .user import User

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    ubicacion = models.CharField('Ubicación', max_length = 300)
    url = models.TextField()

