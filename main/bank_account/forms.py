from django import forms
from django.core.validators import RegexValidator

from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_number', 'balance']
        labels = {
            "balance": "Баланс",
            "account_number": "Номер счёта",
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['account_number'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        instance = super(AccountForm, self).save(commit=False)
        if self.request:
            instance.user = self.request.user
        if commit:
            instance.save()
        return instance


class TransferForm(forms.Form):
    sender_account = forms.ModelChoiceField(
        queryset=Account.objects.none(),
        # widget=forms.HiddenInput(),
        label="Счет"
    )
    receiver = forms.CharField(max_length=150, label="Номер счёта/карты",
                               validators=[
                                   RegexValidator(
                                       regex=r'^\d{16}$|^\d{20}$',
                                       message='Введите номер счёта или номер карты',
                                       code='invalid_account_or_card_number'
                                   )
                               ]
                               )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Сумма перевода',
        widget=forms.NumberInput(attrs={'min': '0', 'step': '0.10', 'placeholder': '0.00', 'type': 'number'}),

    )

    def __init__(self, user, *args, **kwargs):
        super(TransferForm, self).__init__(*args, **kwargs)
        self.fields['sender_account'].queryset = Account.objects.filter(user=user)

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise forms.ValidationError('Сумма перевода не может быть меньше 0.')
        return amount
