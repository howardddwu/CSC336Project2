from django.shortcuts import render
from django.utils import html
from requests.api import get
from .models import Movies
from .connect_api import get_movie_list

def home(request):
    return render(request, "mymovieapp/index.html")


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        movies = Movies.objects.filter(
            title__icontains=searched
        )
        backdrops = [f"https://image.tmdb.org/t/p/w342{m.backdrop_path}" for m in movies]

        context = zip(movies, backdrops)

        return render(
            request, "mymovieapp/search.html", {"searched": searched, "context": context}
        )
    else:
        return render(request, "mymovieapp/search.html", {})

def now_playing(request):
    movies = get_movie_list("now_playing")

    return render(
        request, "mymovieapp/now_playing.html", {"movies": movies} 
    )

def popular(request):
    movies = get_movie_list("popular")

    return render(
        request, "mymovieapp/popular.html", {"movies": movies} 
    )

def single_movie(request, movie_id):

    movie = Movies.objects.get(movie_id=movie_id)
    backdrop = f"https://image.tmdb.org/t/p/w342{movie.backdrop_path}"
    poster = f"https://image.tmdb.org/t/p/w342{movie.poster_path}"

    fav = bool

    if movie.favorites.filter(id=request.user.id).exists():
        fav = True

    return render(
        request, "mymovieapp/single-movie.html", {"movie": movie, "backdrop": backdrop, "poster": poster, "fav": fav}
    )
