from django.db import models

class ComentarioModel(models.Model):
    nombre_torrent = models.CharField(max_length=10000, verbose_name='Nombre de Torrent', blank=False, null=False)
    nombre_usuario = models.CharField(max_length=15, null= False, blank=False, verbose_name="Nombre de Usuario")
    imagen_usuario = models.CharField(null=False, blank=False, verbose_name="Imagen de Usuario")
    texto_usuario = models.TextField(max_length=350, verbose_name='Texto de comentario', blank=True, null=True)
    fecha = models.DateField(verbose_name="Fecha de publicación")

    class Meta:
        db_table = 'comentario'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f"Comentario: {self.nombre_torrent} - {self.nombre_usuario} - [{self.texto_usuario}]"