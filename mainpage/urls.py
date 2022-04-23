from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.MainPage, name='main-page'),
    path('logout', views.logout_user, name='logout'),
   
]
