from django.db import models

class ComentarioModel(models.Model):
    texto = models.TextField(max_length=350, verbose_name='Texto de comentario', blank=True, null=True)
    likes = models.IntegerField(verbose_name="Likes", blank=False, null=False)
    dislikes = models.IntegerField(verbose_name="Dislikes", blank=False, null=False)
    fecha = models.DateTimeField(verbose_name="Fecha de subida") # Se rellenará automaticamente
    es_like = models.ForeignKey(
        'Users.FavoritoModel',
        verbose_name="Dado Like",
        on_delete=models.DO_NOTHING,
        related_name='comentarios_likes'
    )
    es_dislike = models.ForeignKey(
        'Users.FavoritoModel',
        verbose_name="Dado Dislike",
        on_delete=models.DO_NOTHING,
        related_name='comentarios_dislikes'
    )

    class Meta:
        db_table = 'comentario'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-fecha']

    def __str__(self):
        return f"Comentario: {self.id} [{self.texto}]"