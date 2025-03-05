from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[list[dict], None, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    А возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        if "operationAmount" not in transaction:
            continue
        operation_amount = transaction["operationAmount"]
        if "currency" not in operation_amount:
            continue
        currency = operation_amount["currency"]
        if "code" not in currency:
            continue
        code = currency["code"]
        if code == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[list[dict], None, None]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        if "description" not in transaction:
            continue
        description = transaction["description"]
        yield description


def card_number_generator(start: int, stop: int) -> Generator[list[dict], None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for i in range(start, stop+1):
        number = str(i).rjust(16,"0")
        yield number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:16]

