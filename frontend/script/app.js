let tg = window.Telegram.WebApp;

tg.expand();

// tg.setBackgroundColor('rgba(255,118,6,0.71)');
// tg.backgroundColor = 'rgba(255,118,6,0.71)';
tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let worker_count = ''
let rate_amount = ''
let urgent_switch = ''

const { ClickHouse } = require('@clickhouse/client');

async function executeQuery(query, host = 'http://localhost', port = 8123, user = 'default', password = '', database = 'default') {
    const client = new ClickHouse({
        url: host,
        port: port,
        username: user,
        password: password,
        database: database,
    });

    try {
        const response = await client.query(query).toPromise();
        const result = await response.json();
        return result;
    } catch (error) {
        console.error(`Ошибка выполнения запроса: ${error.message}`);
        return null;
    }
}

// Пример использования функции
(async () => {
    const query = 'SELECT * FROM my_table LIMIT 10';
    const result = await executeQuery(query, 'http://my_clickhouse_server', 8123, 'my_user', 'my_password', 'my_database');
    console.log(result);
})();


document.getElementById("go-button").addEventListener("click", function () {
//     TODO: Написать обращение к функции которая будет делать нормальный запрос к бд
});

document.getElementById("nav-button-left").addEventListener("click", function () {
//     TODO: Написать обращение к функции которая будет делать нормальный запрос к бд
});

document.getElementById("nav-button-right").addEventListener("click", function () {
//     TODO: Написать обращение к функции которая будет делать нормальный запрос к бд
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
    tg.HapticFeedback.impactOccurred('medium')
//     TODO: Написать обращение к функции которая будет делать нормальный запрос к бд
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
//     TODO: Написать обращение к функции которая будет делать нормальный запрос к бд
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
//     TODO: Написать обращение к функции которая будет делать нормальный запрос к бд
});

document.getElementById("urgent-switch-button").addEventListener("click", function () {
    const element = document.getElementById("urgent-switch-button");
    const elementInput = document.getElementById('urgent-switch');
    if (parseInt(elementInput.value) === 0) {
        elementInput.value = 1;
        element.style.backgroundColor = "#F66A2A";
        urgent_switch = 1
//     TODO: Написать обращение к функции которая будет делать нормальный запрос к бд
    } else {
        elementInput.value = 0;
        element.style.backgroundColor = "";
        urgent_switch = 0
//     TODO: Написать обращение к функции которая будет делать нормальный запрос к бд
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