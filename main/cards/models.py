import random
import string
from datetime import timedelta
from django.db import models, IntegrityError
from bank_account.models import Account


class Card(models.Model):
    CARD_TYPE_CHOICES = [
        ('debit', 'Дебетовая'),
        ('credit', 'Кредитная'),
    ]
    user = models.CharField(default="from account")
    linked_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.CharField(max_length=16, default="random")
    expiry_date = models.DateField(default="admin check")
    expiry_years = models.PositiveIntegerField(default=0)
    cvv = models.CharField(max_length=3, default="random")
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES, default='debit')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.user = self.linked_account.user.username
        if self.expiry_date and self.expiry_years:
            self.expiry_date = self.expiry_date + timedelta(days=365 * self.expiry_years)
        if self.number == "random":
            self.number = ''.join(random.choice(string.digits) for _ in range(16))
        if self.cvv == "random":
            self.cvv = ''.join(random.choice(string.digits) for _ in range(3))
        while True:
            try:
                super().save(*args, **kwargs)
            except IntegrityError:
                self.number = ''.join(random.choice(string.digits) for _ in range(16))
            else:
                break

    def __str__(self):
        return f"Number: {self.number} | {self.expiry_date} | {self.card_type}"
