"""
Задание 4. Модуль 3. Функции.
Студент: Ветко Андрей Алексеевич.
Группа: БИЗ-Б-0-Д-2024-1.
"""


def calculate_profit(revenue, costs):
    """Возвращает прибыль как разницу между выручкой и затратами."""
    return revenue - costs


def calculate_vat(price, rate=20):
    """Возвращает сумму НДС для цены товара и ставки налога."""
    return price * rate / 100


def get_business_category(revenue):
    """Возвращает категорию бизнеса по годовой выручке."""
    if revenue < 1_000_000:
        return "микро"
    if revenue < 10_000_000:
        return "малый"
    if revenue < 100_000_000:
        return "средний"
    return "крупный"


def compound_interest(capital, rate, years):
    """Возвращает итоговую сумму по формуле сложного процента."""
    return capital * (1 + rate / 100) ** years


def apply_discount(price, discount):
    """Возвращает цену товара после применения скидки."""
    return price * (1 - discount / 100)


if __name__ == "__main__":
    print("1. Расчёт прибыли")
    for revenue, costs in [(120000, 90000), (85000, 70000), (50000, 54000)]:
        print(f"Выручка: {revenue}, затраты: {costs}, прибыль: {calculate_profit(revenue, costs)}")

    print("2. Расчёт НДС")
    print(f"НДС по ставке 20%: {calculate_vat(15000):.2f} руб.")
    print(f"НДС по ставке 10%: {calculate_vat(15000, 10):.2f} руб.")

    print("3. Категория бизнеса")
    for revenue in [500000, 5_000_000, 50_000_000, 150_000_000]:
        print(f"Выручка {revenue}: {get_business_category(revenue)} бизнес")

    print("4. Сложный процент")
    for years in [3, 5, 10]:
        amount = compound_interest(100000, 8, years)
        print(f"Срок {years} лет: {amount:.2f} руб.")

    print("5. Применение скидки")
    for price in [1200, 2500, 800, 4300, 1500]:
        print(f"Цена {price} руб., со скидкой 15%: {apply_discount(price, 15):.2f} руб.")
