def filter_by_state(list_trans: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state(по умолчанию 'EXECUTED').
    И возвращает новый список словарей, содержащий словари, у которых ключ state соответствует указанному значению."""
    new_list: list[dict] = []
    for trans in list_trans:
        if trans.get("state") == state:
            new_list.append(trans)
    return new_list


def sort_by_date(requests: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки.
    И возвращает новый список, отсортированный по дате."""
    return sorted(requests, key=lambda x: x.get("date", ""), reverse=reverse)
