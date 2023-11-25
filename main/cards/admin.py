import random
import string

from django.contrib import admin
from django.db import IntegrityError

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ['user', 'linked_account', 'number', 'cvv']
    readonly_fields = ["number", "cvv"]

    # list_display = ('user', 'linked_account', 'number', 'expiry_date', 'cvv')

    def save_model(self, request, obj, form, change):
        # Генерируем случайный номер карточки, если он не указан
        if not obj.number:
            obj.number = ''.join(random.choice(string.digits) for _ in range(16))

        # Генерируем случайный CVV, если он не указан
        if not obj.cvv:
            obj.cvv = ''.join(random.choice(string.digits) for _ in range(1))

        while True:
            try:
                # Пытаемся сохранить объект
                super().save_model(request, obj, form, change)
            except IntegrityError:
                # Если возникает ошибка IntegrityError (включая ошибку уникальности), генерируем новый номер
                obj.number = ''.join(random.choice(string.digits) for _ in range(16))
            else:
                # Если сохранение прошло успешно, выходим из цикла
                break


admin.site.register(Card, CardAdmin)

