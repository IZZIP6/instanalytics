from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import requests


def index(request):
    return render(request, 'analytics/index.html')


def start(request, username_id):
    try:
        r = requests.get("http://127.0.0.1:5000/s/"+username_id)
        return render(request, 'analytics/user.html', r.json())
    except:
        return render(request, 'analytics/err.html')


def log(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user     = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'analytics/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect(index)


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                confirm  = "Account created for {username}"
                return render(request, 'analytics/register.html', {'confirm': confirm, 'form': form})
            else:
                err = form.errors
                return render(request, 'analytics/register.html', {'err': err, 'form': form})
        else:
            form = UserCreationForm()
        return render(request, 'analytics/register.html', {"form": form})



def download_pdf(request):
    '''
    your code
    :param request:
    :return:
    '''

