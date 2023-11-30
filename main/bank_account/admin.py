from django.contrib import admin
from .models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'balance']
    readonly_fields = ["account_number"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'amount', 'date']
    readonly_fields = ["date"]
# admin.site.register(Account, AccountAdmin)
