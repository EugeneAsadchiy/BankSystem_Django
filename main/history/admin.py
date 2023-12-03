from django.contrib import admin
from history.models import History
from django.urls import reverse
from django.utils.html import format_html


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_type', 'get_related_object', 'timestamp')
    search_fields = ('user__username',)
    list_filter = ('action_type', 'timestamp')

    def get_related_object(self, obj):
        if obj.link:
            if obj.action_type == 'deposit':
                link = reverse('admin:deposit_deposit_change', args=[obj.object_id])
            elif obj.action_type == 'credit':
                link = reverse('admin:credit_credit_change', args=[obj.object_id])
            elif obj.action_type == 'transfer':
                link = reverse('admin:bank_account_transaction_change', args=[obj.object_id])
            elif obj.action_type == 'account':
                link = reverse('admin:bank_account_account_change', args=[obj.object_id])
            elif obj.action_type == 'credit_card':
                link = reverse('admin:cards_card_change', args=[obj.object_id])
            elif obj.action_type == 'debit_card':
                link = reverse('admin:cards_card_change', args=[obj.object_id])

        return format_html('<a href="{}">{}</a>', link, obj.link) if obj.link else None

    get_related_object.short_description = 'Related Object'
