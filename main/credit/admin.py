from django.contrib import admin

# Register your models here.
from credit.models import Credit


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['user', "name", 'interest_rate', 'term_years', "balance"]
    # readonly_fields = ["balance"]
    exclude = ["amount"]
