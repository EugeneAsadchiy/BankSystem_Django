# views.py
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from cards.models import Card
from .models import Credit

from django.views.generic import ListView


@login_required(login_url='login')
def apply_credit(request):
    offers = [
        {'name': 'Кредит наличными', 'amount': 200000, 'interest_rate': 9.9, 'term_years': 5, 'id': 1},
        {'name': 'Кредит под залог недвижимости', 'amount': 1000000, 'interest_rate': 8.9, 'term_years': 15, 'id': 2},
        {'name': 'Автокредит', 'amount': 300000, 'interest_rate': 8.9, 'term_years': 5, 'id': 3},
        {'name': 'Рефинансирование кредитов других банков', 'amount': 200000, 'interest_rate': 9.9, 'term_years': 5,
         'id': 4},
        {'name': 'Ипотека', 'amount': 1000000, 'interest_rate': 5.7, 'term_years': 30, 'id': 5},
        {'name': 'Кредит под залог автомобиля', 'amount': 250000, 'interest_rate': 8.9, 'term_years': 7, 'id': 6},
        # Добавьте другие предложения по мере необходимости
    ]

    user = request.user
    context = {'offers': offers, 'user': user}

    if request.method == 'POST':
        offer_id = int(request.POST.get('offer_id')) - 1
        print(offer_id)
        # print("Offer ID:", offer_id)
        credit = Credit.objects.create(user=user, name=offers[offer_id]["name"], amount=offers[offer_id]["amount"],
                                       interest_rate=offers[offer_id]["interest_rate"],
                                       term_years=offers[offer_id]["term_years"],
                                       balance=offers[offer_id]["amount"])
        # date = datetime.now() + timedelta(days=365 * offers[offer_id]["term_years"])

        # card = Card.objects.create(linked_account=linked_account, expiry_date=datetime.now(),
        #                            expiry_years=credit.term_months, card_type="credit")
        # credit.linked_card = card
        credit.save()
        # form = CreditForm(request.user, request.POST)
        # if form.is_valid():
        #     print("pizda")
        #     credit = form.save(commit=False)
        #     credit.user = request.user
        #     credit.balance = credit.amount
        #
        #     linked_account = form.cleaned_data['linked_account']
        #     linked_account.balance += credit.amount
        #     linked_account.save()
        #     card = Card.objects.create(linked_account=linked_account, expiry_date=datetime.now(),
        #                                expiry_years=credit.term_months, card_type="credit")
        #
        #     credit.linked_card = card
        #     credit.save()
        #     messages.success(request, 'Кредит успешно оформлен.')
        return redirect('apply_credit_successful')
        # else:
        #     print("popa")
        #     # Если форма не прошла валидацию, вернем страницу с формой и ошибками
        #     return render(request, 'credit/apply_credit.html', context)

    # Если запрос не POST (например, GET), просто отрисуем страницу с формой
    return render(request, 'credit/apply_credit.html', context)


class ListCredits(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "credit/my_credits.html"
    model = Credit  # само выберет все данные и передаст в контекст
    context_object_name = "credits"

    def get_queryset(self):
        return Credit.objects.filter(user=self.request.user)


# def transact(request):


def apply_credit_successful(request):
    return render(request, 'credit/apply_credit_successful.html')
