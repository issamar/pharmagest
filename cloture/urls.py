from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.closure, name= 'closure'),
    path('edit/<int:pk>', views.editclo, name='editclo'),
    path('viewall', views.viewall, name='view-all'),
    path('logi/<int:pk>', views.editall, name='edit-all'),

    
]
