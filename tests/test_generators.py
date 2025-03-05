from generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 3


def test_filter_by_currency_empty(transactions):
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0


def test_transaction_descriptions(transactions):
    generator_transaction_descriptions = transaction_descriptions(transactions)
    assert next(generator_transaction_descriptions) == "Перевод организации"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"
    assert next(generator_transaction_descriptions) == "Перевод с карты на карту"
    assert next(generator_transaction_descriptions) == "Перевод организации"


def test_card_number_generator():
    generator_card_number_generator = card_number_generator(1, 5)
    assert next(generator_card_number_generator) == "0000 0000 0000 0001"
    assert next(generator_card_number_generator) == "0000 0000 0000 0002"
