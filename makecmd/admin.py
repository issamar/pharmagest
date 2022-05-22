from django.contrib import admin

from makecmd.models import Mycmd
from .models import Mycmd, StatTable
# Register your models here.
#admin.site.register(Mycmd)
@admin.register(Mycmd)
class CmdAdmin(admin.ModelAdmin):
	list_display = ('product', 'prod_stat', 'cmded', 'received','received_0', 'indisponible','deleted', 'client')
	ordering = ('product',)
	search_fields = ('product',)


@admin.register(StatTable)
class StatTableAdmin(admin.ModelAdmin):
	list_display = ('product', 'cmded', 'received', 'indisponible')
	ordering = ('product',)
	search_fields = ('product',)
