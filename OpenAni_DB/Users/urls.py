from django.urls import path

from Users.views import *

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("users/", UserView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("favorito/", FavoritoView.as_view()),
]