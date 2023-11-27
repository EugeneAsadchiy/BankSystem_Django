import random
import string

from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ['linked_account', 'number', 'cvv']
    readonly_fields = ["number", "cvv"]


admin.site.register(Card, CardAdmin)
