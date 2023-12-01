import random
import string
from datetime import timedelta

from django.db import models, IntegrityError

from django.contrib.auth.models import User
from bank_account.models import Account


class Card(models.Model):
    CARD_TYPE_CHOICES = [
        ('debit', 'Дебетовая'),
        ('credit', 'Кредитная'),
    ]
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(default="from account")
    linked_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.CharField(max_length=16,
                              default="random")  # Предполагается, что номер карточки состоит из 16 символов
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

        # Генерируем случайный CVV, если он не указан
        if self.cvv == "random":
            self.cvv = ''.join(random.choice(string.digits) for _ in range(3))

        # Ограничиваем количество попыток поиска уникального номера
        while True:
            try:
                # Пытаемся сохранить объект
                super().save(*args, **kwargs)
            except IntegrityError:
                # Если возникает ошибка IntegrityError (включая ошибку уникальности), генерируем новый номер
                self.number = ''.join(random.choice(string.digits) for _ in range(16))
            else:
                # Если сохранение прошло успешно, выходим из цикла
                break

    def __str__(self):
        return f"{self.linked_account.account_number} | {self.number} | {self.expiry_date} | {self.card_type}"
