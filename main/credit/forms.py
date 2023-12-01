# forms.py
from django import forms

from bank_account.models import Account
from credit.models import Credit


class CreditForm(forms.ModelForm):
    linked_account = forms.ModelChoiceField(
        queryset=Account.objects.none(),
        label='Выберите счёт',
        empty_label='Выберите счёт'
        # required=True,
    )

    class Meta:
        model = Credit
        fields = ["linked_account", 'amount', 'interest_rate', 'term_months']
        labels = {
            "amount": "Желаемый размер кредита",
            "interest_rate": "Процентная ставка",
            "term_months": "Срок кредита",
        }

    def __init__(self, user, *args, **kwargs):
        super(CreditForm, self).__init__(*args, **kwargs)
        self.fields['linked_account'].queryset = Account.objects.filter(user=user)
