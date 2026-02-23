from rest_framework import serializers

from Users.models import FavoritoModel


class FavoritoSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(required=True)
    nombre_torrent = serializers.CharField(required=True)
    enlace = serializers.CharField(required=True)
    tamano = serializers.CharField(required=True)
    fecha = serializers.CharField(required=True)
    seeders = serializers.CharField(required=True)
    leechers = serializers.CharField(required=True)

    class Meta:
        model = FavoritoModel
        fields = ("nombre_usuario", "nombre_torrent", "enlace", "tamano", "fecha", "seeders", "leechers")