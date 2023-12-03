# models.py

from django.db import models
from django.contrib.auth.models import User

from cards.models import Card
from deposit.models import Deposit

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class History(models.Model):
    ACTION_TYPES = [
        ('credit', 'Оформление кредита'),
        ('credit_card', 'Оформление  кредитной карты'),
        ('debit_card', 'Оформление  дебетовой карты'),
        ('transfer', 'Перевод средств'),
        ('deposit', 'Оформление вклада'),
        ('account', 'Оформление счёта'),
        # Добавьте другие типы действий по мере необходимости
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=20, choices=ACTION_TYPES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    link = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action_type}"

    def save(self, *args, **kwargs):
        self.content_type = ContentType.objects.get_for_model(self.link)
        super().save(*args, **kwargs)
