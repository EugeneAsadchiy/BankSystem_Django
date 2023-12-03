from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.views.generic import ListView

from history.models import History
from .forms import DepositForm
from .models import Deposit


class ListDeposits(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "deposit/my_deposits.html"
    model = Deposit  # само выберет все данные и передаст в контекст
    context_object_name = "deposits"

    def get_queryset(self):
        return Deposit.objects.filter(user=self.request.user)


@login_required(login_url='login')
def create_deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
            # Записываем действие в историю
            action_type = "deposit"  # Замените на актуальный тип действия
            # history = History.objects.create(user=request.user, action_type=action_type, object_id=deposit.pk)
            history = History.objects.create(user=request.user, action_type=action_type,
                                             content_type=ContentType.objects.get_for_model(Deposit),
                                             object_id=deposit.id, link=deposit)
            history.save()

        return redirect('apply_deposit_successful')
    else:
        form = DepositForm()
    return render(request, 'deposit/apply_deposit.html', {'form': form})


def success_url(request):
    return render(request, 'deposit/apply_deposit_successful.html')
