from django.contrib import admin
from .models import Addart, Addmed
# Register your models here.
class MedSearch(admin.ModelAdmin):
    search_fields = ('name',)

class ArtSearch(admin.ModelAdmin):
    search_fields = ('full_name',)
admin.site.register(Addmed, MedSearch)
admin.site.register(Addart, ArtSearch)