from django.db import models

class FavoritoModel(models.Model):
    user = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    torrent = models.ForeignKey("Torrents.TorrentModel", on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'torrent'),)
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"

    def __str__(self):
        return f"User: {self.user} - Torrent: {self.torrent}"