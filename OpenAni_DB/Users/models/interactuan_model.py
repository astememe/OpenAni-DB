from django.db import models
from rest_framework.fields import BooleanField


class InteractuanModel(models.Model):
    es_like = BooleanField(default=False)
    es_dislike = BooleanField(default=False)

    class Meta:
        db_table = "interactuan"
        verbose_name = "Interactuan"
        verbose_name_plural = "Interactuan"

    def __str__(self):
        return f"Liked: {self.es_like} ——— Disliked: {self.es_dislike}"

