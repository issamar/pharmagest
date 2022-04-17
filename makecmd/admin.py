from django.contrib import admin

from makecmd.models import Mycmd
from .models import Mycmd
# Register your models here.
#admin.site.register(Mycmd)
@admin.register(Mycmd)
class CmdAdmin(admin.ModelAdmin):
	list_display = ('product', 'prod_stat', 'cmded', 'received', 'indisponible', 'client')
	ordering = ('product',)
	search_fields = ('product',)