import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView

from bank_account.forms import AccountForm
from bank_account.models import Account


@login_required(login_url='login')
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST, request=request)
        if form.is_valid():
            form.save()
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


def success_url(request):
    return render(request, 'bank_account/order_account_successful.html')
