from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CmdPage, name= 'cmd-page'),
    path('edit/<int:prod_id>', views.editItem, name= 'edit-page'),
]
