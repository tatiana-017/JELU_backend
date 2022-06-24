from authApp.models.solicitud import Solicitud
from rest_framework import serializers

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id','user','razonSolicitud']