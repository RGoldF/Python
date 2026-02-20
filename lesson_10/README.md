# Проект автоматизации тестирования с Allure отчетами

## Описание проекта
Данный проект содержит наборы автоматизированных тестов для двух веб-приложений:
- **Медленный калькулятор**: Проверка операций сложения с настраиваемой задержкой выполнения.  
  URL: [https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
- **Магазин Sauce Demo**: Сквозной сценарий покупки товаров (авторизация -> корзина -> оформление заказа).  
  URL: [https://www.saucedemo.com/](https://www.saucedemo.com/)

В проекте реализован **Page Object Model**, использована строгая типизация параметров (**Type Hinting**) и подробное документирование методов (**Docstrings**).

## Структура проекта
├── calculator_page.py    # Класс страницы калькулятора (методы и локаторы)
├── shop_auth_page.py     # Страница авторизации магазина
├── shop_main_page.py     # Главная страница магазина (выбор товаров)
├── shop_cart_page.py     # Страница корзины магазина
├── shop_order_page.py    # Страница оформления и проверки стоимости заказа
├── conftest.py           # Конфигурация Pytest и фикстуры для браузеров (Chrome/Firefox)
├── test_calculator.py    # Тесты функциональности калькулятора
├── test_shop.py          # Тесты функциональности магазина
├── requirements.txt      # Список зависимостей (selenium, pytest, allure-pytest и др.)
└── README.md             # Документация проекта

## Инструкция по запуску тестов
1. Установите зависимости: `pip install -r requirements.txt`
2. Запуск тестов в разных браузерах (указаны в параметрах тестов):
   - **Chrome**: `pytest test_calculator.py`
   - **Firefox**: `pytest test_shop.py`

## Работа с Allure
### Генерация отчета
Для сбора данных в папку `allure-results` запустите команду:
```bash
pytest --alluredir=allure-results