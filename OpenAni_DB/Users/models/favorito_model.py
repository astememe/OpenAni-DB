from django.db import models
from django.db.models import BooleanField


class FavoritoModel(models.Model):
    users = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    torrents = models.ForeignKey("Torrents.TorrentModel", on_delete=models.CASCADE)

    es_favorito = BooleanField(default=False)
    es_like = BooleanField(default=False)
    es_dislike = BooleanField(default=False)

    def __str__(self):
        return f"favorito = {self.es_favorito}"