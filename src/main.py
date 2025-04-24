from src.finance import read_transactions_from_csv, read_transactions_from_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.regular import get_sort_bank_operations
from src.utils import get_read_json
from src.widget import get_date, mask_account_card


def main():
    """Функция в модуле main, которая отвечает за основную логику проекта и связывает функциональности между собой."""
    transactions = []
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        menu_item = input('''Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
''').strip()
        if menu_item in ['1', '2', '3']:
            if menu_item == '1':
                print("Получить информацию о транзакциях из JSON-файла")
                transactions = get_read_json("../data/operations.json")

            elif menu_item == '2':
                print("Получить информацию о транзакциях из CSV-файла")
                transactions = read_transactions_from_csv("../data/transactions.csv")

            elif menu_item == '3':
                print("Получить информацию о транзакциях из XLSX-файла")
                transactions = read_transactions_from_excel("../data/transactions_excel.xlsx")
            break
        else:
            print("Введите пожалуйста число 1, 2 или 3")

    while True:
        possible_status = ['executed', 'canceled', 'pending']
        status = str(input('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:''')).lower().strip()

        if status in possible_status:
            transactions = filter_by_state(transactions, state=status.upper())
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break

        else:
            print(f'Статус операции "{status}" недоступен')

    while True:
        answer_sort = str(input("Отсортировать операции по дате? Да/Нет:")).lower().strip()
        if answer_sort in ["да", "нет"]:
            if answer_sort == "да":
                while True:
                    answer_sort_size = input("Отсортировать по возрастанию или по убыванию?:").lower().strip()
                    if answer_sort_size == 'по возрастанию':
                        transactions = sort_by_date(transactions, False)
                        break
                    elif answer_sort_size == 'по убыванию':
                        transactions = sort_by_date(transactions)
                        break
                    else:
                        print("Введите по возрастанию или по убыванию")
            break
        else:
            print("Ответьте Да или Нет")

    while True:
        answer_sort_rub = input("Выводить только рублевые тразакции? Да/Нет:").lower().strip()
        if answer_sort_rub in ["да", "нет"]:
            if answer_sort_rub == "да" and menu_item == "1":
                transactions = [transaction for transaction in filter_by_currency(transactions, 'RUB')]
            elif answer_sort_rub == "да":
                transactions = list(filter(lambda x: x["currency_code"] == "RUB", transactions))
            break
        else:
            print("Ответьте Да или Нет")

    while True:
        answer_filter = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет:").lower().strip()

        if answer_filter in ["да", "нет"]:
            if answer_filter == "да":
                print("Введите  определенное слово в описании")
                answer_filter_word = input().lower().strip()
                transactions = get_sort_bank_operations(transactions, answer_filter_word)
            break

        else:
            print("Ответьте Да или Нет")

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        date = str(get_date(transaction.get("date", "")))
        description = transaction.get("description", "")
        to = transaction.get("to", "")
        amount = transaction.get("amount", "")
        state = transaction.get("state", "")
        if menu_item == "1":
            currency_name = transaction.get("operationAmount").get("currency").get("name")
            amount = transaction.get("operationAmount").get("amount", "")
        elif menu_item in ["2", "3"]:
            currency_name = transaction.get("currency_name")
            amount = transaction.get("amount", "")
        if description != "Открытие вклада":
            fro = transaction.get("from", "")
            to_ready = mask_account_card(to)
            fro_ready = mask_account_card(fro)
            print(f"{date} {description}\n{fro_ready} -> {to_ready}\n{float(amount)} {currency_name}\n{state}")
            print()
        else:
            to_ready = mask_account_card(to)
            print(f"{date} {description}\n{to_ready}\n{float(amount)} {currency_name}\n{state}")
            print()

    if transactions == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
