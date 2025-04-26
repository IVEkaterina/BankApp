from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[dict, None, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    А возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in transactions:
        code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, None, None]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        if "description" not in transaction:
            continue
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for i in range(start, stop + 1):
        number = str(i).rjust(16, "0")
        result = number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:16]
        yield result
