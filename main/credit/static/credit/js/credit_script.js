// credit_script.js

function applyCredit(offerId) {
  var offerElement = $(".offer[data-offer-id=" + offerId + "]");
  var amount = offerElement.find("p:contains('Сумма')").text().split(":")[1].trim();
  var interestRate = offerElement.find("p:contains('Процентная ставка')").text().split(":")[1].trim();
  var term = offerElement.find("p:contains('Срок')").text().split(":")[1].trim();

  // Отправляем данные на сервер
  $.ajax({
    type: 'POST',
    url: '/apply_credit/',  // Укажите корректный URL для вашего представления
    data: {
      csrfmiddlewaretoken: '{{ csrf_token }}',
      linked_account: 'Выберите нужный счет',  // Замените этим значением
      amount: amount,
      interest_rate: interestRate,
      term_months: term
    },
    success: function (data) {
      alert("Оформлен новый кредит:\nСумма: " + amount + "\nПроцентная ставка: " + interestRate + "\nСрок: " + term);
      // Добавьте здесь код для обновления страницы или другие действия после успешного оформления кредита
    },
    error: function (xhr, status, error) {
      console.error("Произошла ошибка при оформлении кредита:", status, error);
      // Добавьте здесь код для обработки ошибки, если это необходимо
    }
  });
}
