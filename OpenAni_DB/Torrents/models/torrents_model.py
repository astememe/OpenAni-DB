from django.db import models

class TorrentModel(models.Model):
    nombre = models.CharField(max_length=10000, verbose_name='Nombre', blank=False, null=False)
    categoria = models.CharField(max_length = 100, verbose_name='Categoria', blank=False, null=False)
    enlace = models.CharField(max_length=10000, verbose_name='Enlace', blank=False, null=False)
    tamano = models.CharField(max_length = 100, verbose_name='Tamano', blank=False, null=False)
    fecha = models.CharField(max_length = 100, verbose_name='Fecha', blank=False, null=False)
    seeders = models.CharField(max_length = 100, verbose_name='Seeders', blank=False, null=False)
    leechers = models.CharField(max_length = 100, verbose_name='Leechers', blank=False, null=False)
    likes = models.IntegerField(verbose_name='Likes', blank=False, null=False, default=0)
    dislikes = models.IntegerField(verbose_name='Dislikes', blank=False, null=False, default=0)

    class Meta:
        db_table = 'torrent'
        verbose_name = 'Torrent'
        verbose_name_plural = 'Torrents'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)