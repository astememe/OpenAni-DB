from django.db import models
from rest_framework.exceptions import ValidationError
from rest_framework.fields import BooleanField

class InteractuarModel(models.Model):
    liked = BooleanField(default=False)
    disliked = BooleanField(default=False)

    def validation(self):
        if self.liked and self.disliked:
            raise ValidationError("No puede estar like y dislike al mismo tiempo")

    class Meta:
        db_table = "interactuar"
        verbose_name = "Interactuar"
        verbose_name_plural = "Interactuar"