from django.contrib import admin

# Register your models here.
from credit.models import Credit


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['user', 'interest_rate', 'term_months', "balance"]
    # readonly_fields = ["balance"]
    exclude = ["amount"]
