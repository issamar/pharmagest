from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.addP, name= 'add-P'),
    path('add_patient/', views.addpinfo, name='add-p-info'),
    path('editrest/<int:pk>',views.editrest, name='edit-rest')


    
]