from django.shortcuts import render
from django.http import HttpResponse
from analytics.app import prova

def index(request):
    return render(request, 'analytics/index.html')

def start(request, username_id):
    try:
        context = prova.insert_username(username_id)
        return render(request, 'analytics/user.html', context)
    except:
        return HttpResponse('User not found, try another username')


