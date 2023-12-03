# models.py
from datetime import timedelta, datetime

import django
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from cards.models import Card


class Credit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="Кредит")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_years = models.PositiveIntegerField(default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=django.utils.timezone.now)

    # linked_card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True,
    #                                 verbose_name='Связанная карточка')
    def save(self, *args, **kwargs):
        if self.date and self.term_years:
            self.date = datetime.now() + timedelta(days=365 * self.term_years)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s credit ({self.amount}, {self.term_years} months)"
