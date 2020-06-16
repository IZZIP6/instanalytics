from django.urls import path
from .import views

urlpatterns = [
        path('', views.index, name='index'),
        path('register', views.register,name='register'),
        path('login', views.log,name='login'),
        path('logout', views.logoutUser,name='logout'),
        path('pdf', views.download_pdf, name='pdf'),
        path('<str:username_id>', views.start, name='start'),
        ]
