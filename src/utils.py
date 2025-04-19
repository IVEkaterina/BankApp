import json
from json import JSONDecodeError


def get_read_json(path_file: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях"""
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []
