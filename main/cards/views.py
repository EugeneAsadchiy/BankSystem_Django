from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from bank_account.models import Account
from cards.forms import CardForm
from cards.models import Card


# class CardView(CreateView):
#     model = Card
#     # fields = ["name", "surname"]  # либо "__all__"
#     form_class = CardForm
#     template_name = 'cards/order_card.html'
#     success_url = "/main"

@login_required
def create_card(request):
    user = request.user

    if request.method == 'POST':
        form = CardForm(user, request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = user
            card.save()
            return redirect('main')  # Перенаправьте на страницу успешного создания карты
    else:
        form = CardForm(user)

    return render(request, 'cards/order_card.html', {'form': form})
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
