let tg = window.Telegram.WebApp;

tg.expand();

// tg.setBackgroundColor('rgba(255,118,6,0.71)');
// tg.backgroundColor = 'rgba(255,118,6,0.71)';
tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let worker_count = ''
let rate_amount = ''
let urgent_switch = ''

document.getElementById("go-button").addEventListener("click", function () {
    tg.sendData({go_button: "True"});
});

document.getElementById("nav-button-left").addEventListener("click", function () {
    tg.sendData({previous: "True"});
});

document.getElementById("nav-button-right").addEventListener("click", function () {
    tg.sendData({next: "True"});
});

document.getElementById("worker-count-button").addEventListener("click", function () {
    let countElementText = document.getElementById("worker-count-text");
    let countElementInput = document.getElementById("worker-count");
    let countText = parseInt(countElementText.textContent);
    let countInput = parseInt(countElementInput.value);
    countText = (countText % 5) + 1;
    countInput = (countInput % 5) + 1;
    countElementText.textContent = countText;
    countElementInput.value = countInput
    worker_count = countInput
    tg.sendData({worker_count_data: worker_count});
});

document.getElementById("worker-count-button").addEventListener("click", function () {
    window.navigator.vibrate(100);
});

document.getElementById("rate-decrease").addEventListener("click", function () {
    let amountElementText = document.getElementById("rate-amount-text");
    let amountText = parseInt(amountElementText.textContent.replace('₽', ''));

    let amountElementInput = document.getElementById("rate-amount");
    let amountInput = parseInt(amountElementInput.value);

    if (amountText > 200) amountText -= 50;
    if (amountInput > 200) amountInput -= 50;

    amountElementText.textContent = amountText + '₽';
    amountElementInput.value = amountInput
    rate_amount = amountInput
    tg.sendData({rate_amount_data: rate_amount});
});

document.getElementById("rate-increase").addEventListener("click", function () {
    let amountElementText = document.getElementById("rate-amount-text");
    let amountText = parseInt(amountElementText.textContent.replace('₽', ''));

    let amountElementInput = document.getElementById("rate-amount");
    let amountInput = parseInt(amountElementInput.value);

    if (amountText < 700) amountText += 50;
    if (amountInput < 700) amountInput += 50;

    amountElementText.textContent = amountText + '₽';
    amountElementInput.value = amountInput
    rate_amount = amountInput
    tg.sendData({rate_amount_data: rate_amount});
});

document.getElementById("urgent-switch-button").addEventListener("click", function () {
    const element = document.getElementById("urgent-switch-button");
    const elementInput = document.getElementById('urgent-switch');
    if (parseInt(elementInput.value) === 0) {
        elementInput.value = 1;
        element.style.backgroundColor = "#F66A2A";
        urgent_switch = 1
        tg.sendData({urgent_switch_data: urgent_switch});
    } else {
        elementInput.value = 0;
        element.style.backgroundColor = "";
        urgent_switch = 0
        tg.sendData({urgent_switch_data: urgent_switch});
    }
});


// Функция для открытия модального окна
function openModal() {
    document.getElementById('modalBackground').style.display = 'flex'; // Показываем фон модального окна
}

// Функция для закрытия модального окна
function closeModal() {
    document.getElementById('modalBackground').style.display = 'none'; // Скрываем фон модального окна
}

// Назначаем обработчик события на ссылку
document.getElementById('details-link').addEventListener('click', function (event) {
    event.preventDefault(); // Предотвращаем переход по ссылке
    openModal(); // Вызываем функцию открытия модального окна
});