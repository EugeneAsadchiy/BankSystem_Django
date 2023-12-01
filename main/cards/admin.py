from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['linked_account', 'number', 'cvv']
    list_editable = []
    exclude = ["user"]
    readonly_fields = ["number", "cvv"]

# admin.site.register(Card, CardAdmin)
