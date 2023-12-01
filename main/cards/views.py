import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, ListView

from bank_account.models import Account
from cards.forms import CardForm
from cards.models import Card


@login_required(login_url='login')
def create_card(request):
    user = request.user
    if request.method == 'POST':
        form = CardForm(user, request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = user
            card.save()
            return redirect('order_card_successful')  # Перенаправьте на страницу успешного создания карты
    else:
        form = CardForm(user)

    return render(request, 'cards/order_card.html', {'form': form})


# @login_required(login_url='login')
class ListCards(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "cards/my_cards.html"
    model = Card  # само выберет все данные и передаст в контекст
    context_object_name = "cards"

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

# def transact(request):


def success_url(request):
    return render(request, 'cards/order_card_successful.html')
