from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_detail, name= 'display_detail'),
    path('add_patient', views.addP, name= 'add-P'),
    path('search_patient', views.searchP, name= 'search-P'),
    path('add_patient/', views.addpinfo, name='add-p-info'),
    path('editrest/<int:pk>',views.editrest, name='edit-rest')


    
]