from rest_framework import serializers

from Users.models import FavoritoModel


class FavoritoSerializer(serializers.ModelSerializer):
    torrent_details = serializers.SerializerMethodField()

    class Meta:
        model = FavoritoModel
        fields = ['id', 'user', 'torrent', 'torrent_details']
        extra_kwargs = {'user': {'read_only': True}}
# __pychache__