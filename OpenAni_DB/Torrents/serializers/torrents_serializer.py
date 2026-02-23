from rest_framework import serializers

from Torrents.models import TorrentModel


class TorrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TorrentModel
        fields = '__all__'