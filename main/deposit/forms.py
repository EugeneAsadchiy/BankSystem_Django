# deposit/forms.py
from django import forms
from .models import Deposit


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount', 'term_months', 'interest_rate']
        labels = {
            "amount": "Сумма вклада",
            "term_months": "Срок вклада",
            "interest_rate": "Ставка %",
        }