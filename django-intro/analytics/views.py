from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import requests

def index(request):
    return render(request, 'analytics/index.html')

def start(request, username_id):
    try:
        r = requests.get("http://127.0.0.1:5000/s/"+username_id)
        return render(request, 'analytics/user.html', r.json())
    except:
        return render(request, 'analytics/err.html')


