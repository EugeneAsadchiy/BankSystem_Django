import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView

from bank_account.forms import AccountForm, TransferForm
from bank_account.models import Account, Transaction
from history.models import History


@login_required(login_url='login')
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST, request=request)
        if form.is_valid():
            account=form.save()
            account.save()
            action_type = "account"  # Замените на актуальный тип действия
            history = History.objects.create(user=request.user, action_type=action_type,
                                             content_type=ContentType.objects.get_for_model(Account),
                                             object_id=account.id, link=account)
            history.save()
            return redirect('order_account_successful')
    else:
        form = AccountForm(request=request)

    return render(request, 'bank_account/order_account.html', {'form': form})


class ListAccounts(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "bank_account/my_accounts.html"
    model = Account  # само выберет все данные и передаст в контекст
    context_object_name = "accounts"

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter_qs = queryset.filter(rating__gt=3) #пример
        user = self.request.user
        return queryset.filter(user=user)


@login_required(login_url='login')
def transfer_view(request):
    if request.method == 'POST':
        form = TransferForm(request.user, request.POST)
        if form.is_valid():
            sender_account = form.cleaned_data['sender_account']
            receiver = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']

            # Проверка наличия пользователя с указанным счетом
            try:
                receiver_account = Account.objects.get(account_number=receiver)
            except Account.DoesNotExist:
                messages.error(request, 'Пользователь не найден')
                return redirect('transfer')
            if sender_account.balance >= amount:
                # Выполнение перевода
                sender_account.balance -= amount
                receiver_account.balance += amount

                sender_account.save()
                receiver_account.save()

                # Запись транзакции
                transfer = Transaction.objects.create(sender=sender_account, receiver=receiver_account, amount=amount)
                transfer.save()
                action_type = "transfer"  # Замените на актуальный тип действия
                history = History.objects.create(user=request.user, action_type=action_type,
                                                 content_type=ContentType.objects.get_for_model(Transaction),
                                                 object_id=transfer.id, link=transfer)
                history.save()
                messages.success(request, 'Перевод успешно выполнен')
                return redirect('transfer')
            else:
                messages.error(request, 'Недостаточно средств для выполнения перевода')
    else:
        form = TransferForm(user=request.user)

    return render(request, 'bank_account/transfer.html', {'form': form})


def success_url(request):
    return render(request, 'bank_account/order_account_successful.html')
