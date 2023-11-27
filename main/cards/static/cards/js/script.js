document.addEventListener("DOMContentLoaded", function () {
    const orderButton = document.getElementById("orderButton");
    const overlay = document.getElementById("overlay");
    const closeButton = document.getElementById("close");

    orderButton.addEventListener("click", function () {
        overlay.style.display = "block";
    });

    closeButton.addEventListener("click", function () {
        overlay.style.display = "none";
    });
});
//document.addEventListener("DOMContentLoaded", function () {
//    var orderButton = document.getElementById("orderButton");
//    var overlay = document.getElementById("overlay");
//    var close = document.getElementById("close");
//    var successMessage = document.getElementById("successMessage");
//    var orderForm = document.getElementById("orderForm");
//
//    orderButton.addEventListener("click", function () {
//        // Можно выполнить дополнительные проверки перед отправкой формы
//        // и показать сообщение только в случае успешной отправки
//
//        // Эмулируем успешную отправку формы
//        // Ваш код отправки формы должен быть здесь
//
//        overlay.style.display = "block";
//        successMessage.style.display = "block";
//    });
//
//    close.addEventListener("click", function () {
//        overlay.style.display = "none";
//        successMessage.style.display = "none";
//        // После закрытия окна, производим редирект
//        window.location.href = "/main/";  // Замените "/success-url/" на ваш success_url
//    });
//});
