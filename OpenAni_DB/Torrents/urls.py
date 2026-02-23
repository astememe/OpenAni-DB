from django.urls import path

from Torrents.views import TorrentViews

urlpatterns = [
    path("torrents/", TorrentViews.as_view()),
]
