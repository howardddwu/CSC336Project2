# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from mymovieapp.models import Movies

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account '{username}' has been created!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "users/profile.html", context)


@login_required
def favorite_list(request):
    new = Movies._default_manager.filter(favorites=request.user)
    backdrops = [f"https://image.tmdb.org/t/p/w342{m.backdrop_path}" for m in new]
    context = zip(new, backdrops)
    return render(request, 'users/favorites.html', {'context': context})


@login_required
def favorite_add(request, movie_id):
    movie = get_object_or_404(Movies, movie_id=movie_id)
    if movie.favorites.filter(id=request.user.id).exists():
        movie.favorites.remove(request.user)
    else:
        movie.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def watch_add(request, id):
    pass
