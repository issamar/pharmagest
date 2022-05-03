from django.contrib import admin
from mainpage.models import Account, UserPayementStat
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class AcountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizeUserAdmin (UserAdmin):
    inlines = (AcountInline, )
admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)


admin.site.register(UserPayementStat)