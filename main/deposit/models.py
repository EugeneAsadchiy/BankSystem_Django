from datetime import timedelta, datetime

import django
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.contenttypes.fields import GenericRelation


class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    term_months = models.PositiveIntegerField(default=0)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField(default=django.utils.timezone.now)
    end_date = models.DateField(blank=True, null=True)
    expected_sum = models.IntegerField(default=0)

    def __str__(self):
        return f"Deposit {self.user.username} - {self.amount} {self.end_date}"

    def calculate_deposit(self, amount, term_months, interest_rate):
        monthly_interest_rate = interest_rate / (12 * 100)
        final_amount = amount * (1 + monthly_interest_rate) ** term_months
        return final_amount

    def save(self, *args, **kwargs):
        # Рассчитываем дату окончания вклада
        self.end_date = self.start_date + timedelta(days=30 * self.term_months)
        self.expected_sum = self.calculate_deposit(self.amount, self.term_months, self.interest_rate)
        super().save(*args, **kwargs)
