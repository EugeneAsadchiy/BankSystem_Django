# models.py
from django.db import models
from django.contrib.auth.models import User

from cards.models import Card


class Credit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_months = models.IntegerField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    linked_card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Связанная карточка')

    def __str__(self):
        return f"{self.user.username}'s credit ({self.amount}, {self.term_months} months)"
