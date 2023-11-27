from django.contrib import admin
from .models import Account


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'balance']
    readonly_fields = ["account_number"]


admin.site.register(Account, AccountAdmin)
