from rest_framework import serializers

from ..models import TorrentModel

class TorrentSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required = True)

    class Meta:
        model = TorrentModel
        fields = '__all__'