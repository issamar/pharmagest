from django.contrib import admin
from .models import Contact
# Register your models here.
#admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'subject')
	search_fields = ('user_name',' subject')