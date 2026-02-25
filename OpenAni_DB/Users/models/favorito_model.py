from django.db import models

class FavoritoModel(models.Model):
    # user = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    # torrent = models.ForeignKey("Torrents.TorrentModel", on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=10000, verbose_name='Nombre Usuario', blank=False, null=False)
    title = models.CharField(max_length=10000, verbose_name='Nombre Torrent', blank=False, null=False)
    magnet = models.CharField(max_length=10000, verbose_name='Enlace', blank=False, null=False)
    size = models.CharField(max_length = 100, verbose_name='Tamano', blank=False, null=False)
    time = models.CharField(max_length = 100, verbose_name='Fecha', blank=False, null=False)
    seeders = models.CharField(max_length = 100, verbose_name='Seeders', blank=False, null=False)
    leechers = models.CharField(max_length = 100, verbose_name='Leechers', blank=False, null=False)
    # likes = models.IntegerField(verbose_name='Likes', blank=False, null=False, default=0)
    # dislikes = models.IntegerField(verbose_name='Dislikes', blank=False, null=False, default=0)

    class Meta:
        # unique_together = (('user', 'torrent'),)
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"

    def __str__(self):
        return f"User: {self.nombre_usuario} - Torrent: {self.title}"