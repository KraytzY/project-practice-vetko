"""
Задание 4. Мини-проект. Вариант 4: учёт доходов и расходов бюджета.
Студент: Ветко Андрей Алексеевич.
Группа: БИЗ-Б-0-Д-2024-1.
"""


def read_items(kind):
    """Запрашивает у пользователя список статей бюджета."""
    count = int(input(f"Введите количество статей {kind}: "))
    items = []
    for number in range(1, count + 1):
        name = input(f"Название статьи {number}: ")
        amount = float(input(f"Сумма статьи {number}: "))
        items.append([name, amount])
    return items


def calculate_total(items):
    """Возвращает общую сумму по списку статей бюджета."""
    total = 0
    for item in items:
        total += item[1]
    return total


def print_items(title, items):
    """Выводит статьи бюджета в понятном виде."""
    print()
    print(title)
    for item in items:
        print(f"{item[0]}: {item[1]:.2f} руб.")


def print_report(incomes, expenses):
    """Выводит итоговый отчёт по доходам и расходам."""
    income_total = calculate_total(incomes)
    expense_total = calculate_total(expenses)
    balance = income_total - expense_total
    print_items("Доходы", incomes)
    print_items("Расходы", expenses)
    print()
    print(f"Итого доходов: {income_total:.2f} руб.")
    print(f"Итого расходов: {expense_total:.2f} руб.")
    print(f"Остаток: {balance:.2f} руб.")
    if balance >= 0:
        print("Заключение: профицит бюджета")
    else:
        print("Заключение: дефицит бюджета")


if __name__ == "__main__":
    print("Учёт доходов и расходов бюджета")
    incomes = read_items("доходов")
    expenses = read_items("расходов")
    print_report(incomes, expenses)
