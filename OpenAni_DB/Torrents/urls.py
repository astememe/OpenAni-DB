from django.urls import path
from .views import TorrentViews

urlpatterns = [
    path("torrents/", TorrentViews.as_view()),
]