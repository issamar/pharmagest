from django.contrib import admin
from django.urls import path, include
from .views import ProductStat
from prods_status import views

urlpatterns = [
    path('',views.ProductStat, name= 'prod-status'),

]
