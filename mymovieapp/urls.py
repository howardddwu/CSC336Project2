from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="main-home"),
    path("search/", views.search, name="main-search"),
    path("movies/", views.movies, name="main-movies"),
    path("nowplaying/", views.now_playing, name="main-nowplaying"),
    path("detail/<int:movie_id>/", views.single_movie, name="movie-detail"),
]