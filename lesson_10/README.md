# NikhomeworkPython
# Урок 10 — PageObject + Allure

## Структура

- `pages/` — PageObject-классы страниц (логин, товары, корзина, checkout, калькулятор).
- `tests/` — UI-тесты под `pytest`:
  - `test_shop.py` — сценарий покупки трёх товаров.
  - `test_calculator.py` — тест медленного калькулятора.
- `conftest.py` — фикстура `driver` для работы с Selenium.
- `allure_results/` — папка для результатов прогона тестов (может быть пустой).
- `allure_report/` — папка для сгенерированного отчёта Allure (в репозиторий не пушится).

## Зависимости

Минимальные зависимости для запуска:

```bash
pip install pytest selenium allure-pytest
