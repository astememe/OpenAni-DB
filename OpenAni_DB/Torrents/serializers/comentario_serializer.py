from rest_framework import serializers

from Torrents.models import ComentarioModel


class ComentarioSerializer(serializers.ModelSerializer):
    nombre_torrent = serializers.CharField(required=True)
    nombre_usuario = serializers.CharField(required=True)
    imagen_usuario = serializers.CharField(required=True)
    texto_usuario = serializers.CharField(required=True)
    fecha = serializers.DateField(required=True)

    class Meta:
        model = ComentarioModel
        fields = ("nombre_torrent", "nombre_usuario", "imagen_usuario", "texto_usuario", "fecha")
