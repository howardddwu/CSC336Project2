from django.shortcuts import render
from django.utils import html
from requests.api import get
from .models import Movies
from .connect_api import get_now_playing
from mymovieapp import connect_api

def home(request):
    return render(request, "mymovieapp/index.html")


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        movies = Movies.objects.filter(
            name_contains=searched
        )

        return render(
            request, "mymovieapp/search.html", {"searched": searched, "movies": movies}
        )
    else:
        return render(request, "mymovieapp/search.html", {})

def now_playing(request):
    movies = get_now_playing()

    return render(
        request, "mymovieapp/now_playing.html", {"movies": movies} 
    )

def movies(request):

    return render(
        request, "mymovieapp/movies.html", {}
    )

def single_movie(request, movie_id):

    movies = {}

    return render(
        request, "mymovieapp/single-movie.html", movies
    )
