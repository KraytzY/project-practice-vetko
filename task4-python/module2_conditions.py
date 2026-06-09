"""
Задание 4. Модуль 2. Условные конструкции и циклы.
Студент: Ветко Андрей Алексеевич.
Группа: БИЗ-Б-0-Д-2024-1.
"""


def exercise_01_financial_result():
    """Определяет финансовый результат периода по значению прибыли."""
    profit = float(input("Введите прибыль за отчётный месяц: "))
    print("1. Финансовый результат периода")
    if profit > 0:
        print("Прибыль")
    elif profit < 0:
        print("Убыток")
    else:
        print("Безубыточность")


def exercise_02_business_category():
    """Определяет категорию бизнеса по годовой выручке."""
    revenue = float(input("Введите годовую выручку предприятия: "))
    print("2. Классификация субъекта по выручке")
    if revenue < 1_000_000:
        print("Микробизнес")
    elif revenue < 10_000_000:
        print("Малый бизнес")
    elif revenue < 100_000_000:
        print("Средний бизнес")
    else:
        print("Крупный бизнес")


def exercise_03_income_tax():
    """Рассчитывает НДФЛ 13 процентов и сумму на руки."""
    salary = float(input("Введите ежемесячную заработную плату: "))
    tax = salary * 0.13
    net_salary = salary - tax
    print("3. Расчёт НДФЛ")
    print(f"НДФЛ: {tax:.2f} руб.")
    print(f"Сумма на руки: {net_salary:.2f} руб.")


def exercise_04_goods_budget():
    """Проверяет доступность пяти товаров в рамках бюджета покупателя."""
    budget = float(input("Введите бюджет покупателя: "))
    print("4. Доступность товаров в рамках бюджета")
    for number in range(1, 6):
        name = input(f"Введите название товара {number}: ")
        price = float(input(f"Введите цену товара {number}: "))
        if price <= budget:
            print(f"{name}: доступен")
        else:
            shortage = price - budget
            print(f"{name}: не хватает {shortage:.2f} руб.")


def exercise_05_half_year_revenue():
    """Анализирует выручку за шесть месяцев."""
    revenues = []
    print("5. Анализ выручки за полугодие")
    for month in range(1, 7):
        value = float(input(f"Введите выручку за месяц {month}: "))
        revenues.append(value)
    average = sum(revenues) / len(revenues)
    print(f"Минимальная выручка: {min(revenues):.2f} руб.")
    print(f"Максимальная выручка: {max(revenues):.2f} руб.")
    print(f"Среднемесячная выручка: {average:.2f} руб.")


if __name__ == "__main__":
    exercise_01_financial_result()
    exercise_02_business_category()
    exercise_03_income_tax()
    exercise_04_goods_budget()
    exercise_05_half_year_revenue()
