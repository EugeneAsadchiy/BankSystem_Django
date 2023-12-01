# views.py
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

import cards.models
from cards.models import Card
from .models import Credit
from .forms import CreditForm


@login_required(login_url='login')
def apply_credit(request):
    if request.method == 'POST':
        form = CreditForm(request.user, request.POST)
        if form.is_valid():
            credit = form.save(commit=False)
            credit.user = request.user
            credit.balance = credit.amount  # начальный баланс считаем равным сумме кредита
            # credit.save()

            linked_account = form.cleaned_data['linked_account']
            linked_account.balance += credit.amount
            linked_account.save()
            card = Card.objects.create(linked_account=linked_account, expiry_date=datetime.now(),
                                       expiry_years=credit.term_months, card_type="credit")

            credit.linked_card = card
            credit.save()
            messages.success(request, 'Кредит успешно оформлен.')
            return redirect('apply_credit')
    else:
        form = CreditForm(user=request.user)

    return render(request, 'credit/apply_credit.html', {'form': form})
