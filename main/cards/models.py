from django.db import models
from django.contrib.auth.models import User
from bank_account.models import Account


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    linked_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.CharField(max_length=16)  # Предполагается, что номер карточки состоит из 16 символов
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s Card"

