from django.db import models
from .user import User

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    razonSolicitud = models.TextField()
