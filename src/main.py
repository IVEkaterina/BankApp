from src.finance import read_transactions_from_csv, read_transactions_from_excel
from src.processing import sort_by_date, filter_by_state
from src.utils import get_read_json


def main():
    print('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')


    while True:
        menu_item = input().strip()

        if menu_item == '1':
            print("Получить информацию о транзакциях из JSON-файла")
            transactions = get_read_json("../data/operations.json")
            break

        elif menu_item == '2':
            print("Получить информацию о транзакциях из CSV-файла")
            transactions = read_transactions_from_csv("../data/transactions.csv")
            break

        elif menu_item == '3':
            print("Получить информацию о транзакциях из XLSX-файла")
            transactions = read_transactions_from_excel("../data/transactions_excel.xlsx")
            break

        else:
            print("Ведите пожалуйста число 1, 2 или 3")


    while True:
        print('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

        possible_status = ['executed', 'canceled', 'pending']

        status = str(input()).lower().strip()

        if status in possible_status:
            transactions = filter_by_state(transactions)
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break

        else:
            print(f'Статус операции "{status}" недоступен')


    while True:
        print("Отсортировать операции по дате? Да/Нет")
        answer_sort = str(input()).lower().strip()
        if answer_sort == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                answer_sort_size = input().lower().strip()
                if answer_sort_size == 'по возрастанию':
                    transactions = sort_by_date(transactions, False)
                    break
                elif answer_sort_size == 'по убыванию':
                    transactions = sort_by_date(transactions)
                    break
                else:
                    print("Введите по возрастанию или по убыванию")
            break
        elif answer_sort == "нет":
            break
        else:
            print("Ответьте Да или Нет")


    while True:
        print("Выводить только рублевые тразакции? Да/Нет")
        answer_sort_rub = input().lower().strip()
        if answer_sort_rub == "да":
            print(1)
        elif answer_sort == "нет":
            break
        else:
            print("Ответьте Да или Нет")


print(main())
