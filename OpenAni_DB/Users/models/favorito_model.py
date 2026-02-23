from django.db import models
from django.db.models import BooleanField


class FavoritoModel(models.Model):
    es_favorito = BooleanField(default=False)

    def __str__(self):
        return f"favorito = {self.es_favorito}"