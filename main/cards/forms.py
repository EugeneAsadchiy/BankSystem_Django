from django import forms
from .models import Card
from .models import Account


# class CardForm(forms.ModelForm):
#     class Meta:
#         model = Card
#         fields = ["linked_account", "expiry_years"]
#         # fields = "__all__"
#         # exclude=["rating"]
#         labels = {
#             "linked_account": "Счет",
#             "expiry_date": "Начало действия карты",
#             "expiry_years": "Срок действия",
#
#         }
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['linked_account', 'expiry_date', 'expiry_years']

        labels = {
            "linked_account": "Счёт",
            "expiry_date": "Дата начала",
            "expiry_years": "Срок службы (лет)",
        }

    def __init__(self, user, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        # фильтруем linked_account для текущего пользователя
        self.fields['linked_account'].queryset = Account.objects.filter(user=user)
        # добавляем атрибут type для expiry_date, чтобы использовать input type="date"
        # self.fields['expiry_date'].widget.attrs.update({'type': 'date'})
        self.fields['expiry_date'].widget = forms.DateInput(attrs={'type': 'date'})
