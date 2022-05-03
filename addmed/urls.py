from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AddMed, name= 'add-med'),
    path('dechiffrage/', views.dech, name='dech')
]
