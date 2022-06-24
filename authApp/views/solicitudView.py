from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from authApp.serializers.solicitudSerializer import SolicitudSerializer

class SolicitudView(views.APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):

        serializer = SolicitudSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response( data={'mensaje': 'Solicitud registrada'}, status=status.HTTP_201_CREATED)