from django.shortcuts import render
from django.utils import html
from requests.api import get
from .models import Movies
from .connect_api import get_now_playing

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
    movies = []
    for movie in get_now_playing()["results"]:
        movies["movie_id"] = movie["id"]
        movies["title"] = movie["title"]
        movies["overview"] = movie["overview"]
        poster = movie["poster_path"]
        movies["image"] = f"https://image.tmdb.org/t/p/w342{poster}"
        movies.append(movie)


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
