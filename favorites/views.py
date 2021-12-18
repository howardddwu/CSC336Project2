from django.shortcuts import render

favorites = []

# Create your views here.
def index(request):
    return render(request, "favorites/index.html", {
        "favorites": favorites
    })

