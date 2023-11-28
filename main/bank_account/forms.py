from django import forms
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
