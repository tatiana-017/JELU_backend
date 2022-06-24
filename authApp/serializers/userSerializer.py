from rest_framework import serializers
from authApp.models.user import User
from authApp.models.video import Video
from authApp.serializers.videoSerializer import VideoSerializer

class UserSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'video']

    def create(self, validated_data):
        videoData = validated_data.pop('video')
        userInstance = User.objects.create(**validated_data)
        Video.objects.create(user=userInstance, **videoData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        video = Video.objects.get(user=obj.id)       
        return {
                    'id': user.id, 
                    'username': user.username,
                    'password': user.password,
                    'name': user.name,
                    'email': user.email,
                    'video': {
                        'id': video.id,
                        'titulo': video.titulo,
                        'fecha': video.fecha,
                        'ubicacion': video.ubicacion,
                        'url': video.url
                    }
                }