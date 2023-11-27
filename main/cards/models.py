import random
import string

from django.db import models, IntegrityError

from django.contrib.auth.models import User
from bank_account.models import Account


class Card(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(default="from account")
    linked_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.CharField(max_length=16,
                              default="random")  # Предполагается, что номер карточки состоит из 16 символов
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3, default="random")

    def save(self, *args, **kwargs):
        self.user = self.linked_account.user.username
        print(self.user)
        # Генерируем случайный номер карточки, если он не указан
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
        return f"{self.linked_account.account_number} | {self.expiry_date} | {self.cvv}"
