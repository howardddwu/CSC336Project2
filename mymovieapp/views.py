from django.shortcuts import render, redirect
from django.urls import reverse
from mymovieapp.models import Users

# Create your views here.
def login(request):
    return render(request,'login.html')

def dologin(request):
    try:
        uname = request.POST.get('username')
        pw = request.POST.get('password')
        obj = Users.objects.get(username = uname)
        correctPW = obj.password
        if(pw != correctPW):
            context = {"msg" : "Incorrect password!"}
        else:
            return render(request,'main.html')
    except Exception as err:
        context = {"msg" : "User Not Found!"}
    return render(request, 'login.html', context)


def signup(request):
    return render(request,'signup.html')

def accUpdate(request):
    uname = request.POST.get('username')
    pw = request.POST.get('password')
    obj = Users()
    obj.username = uname
    obj.password = pw
    obj.save()
    return render(request,'login.html')