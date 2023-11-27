import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, ListView

from bank_account.models import Account
from cards.forms import CardForm
from cards.models import Card


# class CardView(CreateView):
#     model = Card
#     # fields = ["name", "surname"]  # либо "__all__"
#     form_class = CardForm
#     template_name = 'cards/order_card.html'
#     success_url = "/main"

# @login_required(login_url='login')
def create_card(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Пожалуйста, авторизуйтесь, чтобы оформить карту.')
        return redirect('login')  # Перенаправление на страницу входа
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


class ListCards(ListView):
    template_name = "cards/my_cards.html"
    model = Card  # само выберет все данные и передаст в контекст
    context_object_name = "cards"

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter_qs = queryset.filter(rating__gt=3) #пример
        return queryset


# def order_card(request):
#     if request.method == 'POST':
#         account_id = request.POST.get('account')
#         account = Account.objects.get(id=account_id)
#         # Обработка данных из формы и создание объекта Card
#         user = "from account"  # Предполагается, что пользователь авторизован
#         linked_account = "12"  # Получаем первый счет пользователя (предположим, что у пользователя только один счет)
#         number = 'random'  # Генерация случайного номера (ваш код генерации)
#         expiry_date = '2023-01-01'  # Замените эту дату на вашу логику
#         cvv = 'random'  # Генерация случайного CVV (ваш код генерации)
#
#         card = Card(user=user, linked_account=account, number=number, expiry_date=expiry_date, cvv=cvv)
#         card.save()
#
#         return render(request, 'cards/order_card.html')
#
#     return render(request, 'cards/order_card.html')
def success_url(request):
    return render(request, 'cards/order_card_successful.html')
