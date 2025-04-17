import json
from json import JSONDecodeError


def get_read_json(path_file: str) -> list[dict]:
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError as f:
        return []
    except JSONDecodeError as j:
        return []
