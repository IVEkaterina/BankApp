import re
from collections import Counter


def get_sort_bank_operations(operations: list[dict], search_string: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращает список словарей, у котороого в описании есть данная строка.
    """

    pattern = re.compile(search_string, re.I)
    result = []
    for oper in operations:
        if ('description' in oper) and (pattern.search(oper['description'])):
            result.append(oper)
    return result


def count_operations_by_category(transactions: list[dict], categories: list) -> dict:
    """Функцию, которая принимает список словарей с данными о банковских операциях и список категорий операций,
     а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    operations = []
    for trans in transactions:
        if 'description' in trans:
            if trans['description'] in categories:
                operations.append(trans['description'])
    return Counter(operations)
