from django.db import models


class Torrent(models.Model):
    titulo = models.CharField(max_length=200)
    tamano = models.CharField(max_length=50)
    fecha = models.CharField(max_length=20)
    categoria = models.CharField(max_length=100)
    seeders = models.IntegerField()
    leechers = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    link = models.CharField()

    class Meta:
        db_table = "torrents"
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.titulo} - {self.categoria}"
