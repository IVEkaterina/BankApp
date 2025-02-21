def filter_by_state(list_trans: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state(по умолчанию 'EXECUTED').
    И возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению."""
    new_list: list[dict] = []
    for trans in list_trans:
        if trans.get("state") == state:
            new_list.append(trans)
    return new_list


list_of_dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

state = input()
if state != "EXECUTED" and state != "CANCELED":
    state = "EXECUTED"

filter_by_state(list_of_dictionaries, state)


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
  """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
  И возвращает новый список, отсортированный по дате."""
  return sorted(data, key=lambda x: x.get("date", ""), reverse=reverse)

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2999-67-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-14T09:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '9998-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

sort_by_date(data)