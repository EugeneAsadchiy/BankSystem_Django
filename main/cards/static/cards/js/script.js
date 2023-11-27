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
