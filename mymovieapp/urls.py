from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="movie-home"),
    path("", views.home, name="main-home"),
    path("search/", views.search, name="movie-search"),
    path("popular/", views.popular, name="popular"),
    path("nowplaying/", views.now_playing, name="nowplaying"),
    path("detail/<int:movie_id>/", views.single_movie, name="movie-detail"),
]