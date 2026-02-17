from django.db import models
from django.db.models import TextField
from rest_framework.fields import IntegerField


class ComentarioModel(models.Model):
    texto = TextField(max_length=500)
    likes = IntegerField()
    dislikes = IntegerField()
    fecha = TextField(max_length=20)

    class Meta:
        db_table = "comentarios"
        ordering = ["-fecha"]
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
