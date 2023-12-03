# deposit/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import DepositForm
from .models import Deposit
from django.http import JsonResponse


class ListDeposits(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "deposit/my_deposits.html"
    model = Deposit  # само выберет все данные и передаст в контекст
    context_object_name = "deposits"

    def get_queryset(self):
        return Deposit.objects.filter(user=self.request.user)


def create_deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
            return redirect('apply_deposit_successful')
    else:
        form = DepositForm()
    return render(request, 'deposit/apply_deposit.html', {'form': form})


def success_url(request):
    return render(request, 'deposit/apply_deposit_successful.html')



