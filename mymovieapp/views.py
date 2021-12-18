from django.shortcuts import render
from django.utils import html


def home(request):
    return render(request, "mymovieapp/index.html")


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        movies = []

        return render(
            request, "mymovieapp/search.html", {"searched": searched, "movies": movies}
        )
    else:
        return render(request, "mymovieapp/search.html", {})

def movies(request):

    return render(
        request, "mymovieapp/movies.html", {}
    )

def single_movie(request, movie_id):

    context = {}

    return render(
        request, "mymovieapp/single-movie.html", context
    )
