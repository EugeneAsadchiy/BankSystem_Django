from django.contrib import admin

# Register your models here.
from deposit.models import Deposit


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['user', "amount", 'term_months', 'interest_rate', "start_date", "end_date", "expected_sum"]
    readonly_fields = ["expected_sum"]
    # exclude = ["amount"]
