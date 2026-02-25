from rest_framework import serializers

from Users.models import FavoritoModel


class FavoritoSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(required=False)
    title = serializers.CharField(required=True)
    magnet = serializers.CharField(required=True)
    size = serializers.CharField(required=True)
    time = serializers.CharField(required=True)
    seeders = serializers.CharField(required=True)
    leechers = serializers.CharField(required=True)

    class Meta:
        model = FavoritoModel
        fields = ("nombre_usuario", "title", "magnet", "size", "time", "seeders", "leechers")