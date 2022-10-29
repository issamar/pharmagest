from re import template
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.MainPage, name='main-page'),
    path('register', views.RegisterPage, name='register'),
    path('logout', views.logout_user, name='logout'),
    
   
]
