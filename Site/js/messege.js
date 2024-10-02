// Открытие модального окна при клике на ссылку
document.getElementById("userAgreementLink").addEventListener("click", function(event) {
    event.preventDefault(); // Предотвращаем переход по ссылке
    document.getElementById("userAgreementModal").style.display = "block";
});

// Закрытие модального окна при клике на кнопку "Закрыть" или вне окна
var modal = document.getElementById("userAgreementModal");
var closeBtn = document.getElementsByClassName("close")[0];
window.onclick = function(event) {
    if (event.target == modal || event.target == closeBtn) {
        modal.style.display = "none";
    }
}







