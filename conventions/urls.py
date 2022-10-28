from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.brd, name= 'brd'),
    path('editBrd/<int:pk>', views.editBrd, name= 'edit-brd'),



    
]