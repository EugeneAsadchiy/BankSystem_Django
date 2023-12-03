import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, ListView

from bank_account.models import Account
from cards.forms import CardForm
from cards.models import Card
from history.models import History


@login_required(login_url='login')
def create_card_debit(request):
    user = request.user
    if request.method == 'POST':
        form = CardForm(user, request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = user
            card.save()
            action_type = "debit_card"  # Замените на актуальный тип действия
            # history = History.objects.create(user=request.user, action_type=action_type, object_id=deposit.pk)
            history = History.objects.create(user=request.user, action_type=action_type,
                                             content_type=ContentType.objects.get_for_model(Card),
                                             object_id=card.id, link=card)
            history.save()
            return redirect('order_card_successful')  # Перенаправьте на страницу успешного создания карты
    else:
        form = CardForm(user)

    return render(request, 'cards/order_card_debit.html', {'form': form})


@login_required(login_url='login')
def create_card_credit(request):
    user = request.user
    if request.method == 'POST':
        form = CardForm(user, request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = user
            card.card_type = "credit"
            card.save()
            action_type = "credit_card"  # Замените на актуальный тип действия
            # history = History.objects.create(user=request.user, action_type=action_type, object_id=deposit.pk)
            history = History.objects.create(user=request.user, action_type=action_type,
                                             content_type=ContentType.objects.get_for_model(Card),
                                             object_id=card.id, link=card)
            history.save()
            return redirect('order_card_successful')  # Перенаправьте на страницу успешного создания карты
    else:
        form = CardForm(user)

    return render(request, 'cards/order_card_credit.html', {'form': form})


# @login_required(login_url='login')
class ListCards(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "cards/my_cards.html"
    model = Card  # само выберет все данные и передаст в контекст
    context_object_name = "cards"

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)


def success_url(request):
    return render(request, 'cards/order_card_successful.html')
