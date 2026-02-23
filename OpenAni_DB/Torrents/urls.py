from django.urls import path

from Torrents.views import TorrentViews
from Users.views.comentario_view import ComentarioView

urlpatterns = [
    path("torrents/", TorrentViews.as_view()),
    path("comentarios/", ComentarioView.as_view()),
]
