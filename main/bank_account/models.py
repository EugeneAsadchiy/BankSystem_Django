import random
import string

from django.db import models, IntegrityError
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, default="random")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Генерируем случайный номер карточки, если он не указан
        if self.account_number == "random":
            self.account_number = ''.join(random.choice(string.digits) for _ in range(20))

        # Ограничиваем количество попыток поиска уникального номера
        while True:
            try:
                # Пытаемся сохранить объект
                super().save(*args, **kwargs)
            except IntegrityError:
                # Если возникает ошибка IntegrityError (включая ошибку уникальности), генерируем новый номер
                self.account_number = ''.join(random.choice(string.digits) for _ in range(20))
            else:
                # Если сохранение прошло успешно, выходим из цикла
                break

    def __str__(self):
        return f"{self.user.username}'s account ({self.account_number})"


class Transaction(models.Model):
    sender = models.ForeignKey(Account, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
