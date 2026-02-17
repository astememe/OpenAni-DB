from django.db import models
from rest_framework.fields import BooleanField


class FavoriteModel(models.Model):
    es_favorito = BooleanField(default=False)

    class Meta:
        db_table = "favoritos"
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"