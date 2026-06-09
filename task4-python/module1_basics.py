"""
Задание 4. Модуль 1. Переменные, типы данных, ввод и вывод.
Студент: Ветко Андрей Алексеевич.
Группа: БИЗ-Б-0-Д-2024-1.
"""


def exercise_01_employee_card():
    """Выводит карточку сотрудника с переменными разных типов."""
    name = "Иван Петров"
    age = 24
    salary = 58000.50
    is_employed = True
    print("1. Карточка сотрудника")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Заработная плата: {salary} руб.")
    print(f"Работает сейчас: {is_employed}")


def exercise_02_greeting():
    """Запрашивает имя и город, затем выводит приветствие сотрудника."""
    name = input("Введите имя сотрудника: ")
    city = input("Введите город: ")
    print("2. Приветствие сотрудника")
    print(f"Сотрудник {name} работает в офисе {city}")


def exercise_03_total_price():
    """Считает итоговую стоимость товара по цене и количеству."""
    price = float(input("Введите цену единицы товара: "))
    quantity = int(input("Введите количество единиц товара: "))
    total_price = price * quantity
    print("3. Расчёт итоговой стоимости")
    print(f"Итоговая стоимость: {total_price:.2f} руб.")


def exercise_04_deposit_income():
    """Считает доход по банковскому вкладу за один год."""
    deposit = float(input("Введите сумму вклада: "))
    rate = float(input("Введите процентную ставку: "))
    income = deposit * rate / 100
    final_amount = deposit + income
    print("4. Доход по банковскому вкладу")
    print(f"Доход за год: {income:.2f} руб.")
    print(f"Итоговая сумма: {final_amount:.2f} руб.")


def exercise_05_currency_conversion():
    """Переводит сумму в рублях в доллары по введённому курсу."""
    usd_rate = float(input("Введите курс доллара к рублю: "))
    rubles = float(input("Введите сумму в рублях: "))
    dollars = round(rubles / usd_rate, 2)
    print("5. Конвертация валюты")
    print(f"Сумма в долларах: {dollars}")


if __name__ == "__main__":
    exercise_01_employee_card()
    exercise_02_greeting()
    exercise_03_total_price()
    exercise_04_deposit_income()
    exercise_05_currency_conversion()
