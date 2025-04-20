import json
import logging
from json import JSONDecodeError

logger = logging.getLogger('__name__')
file_handler = logging.FileHandler("../logs/utils.log", encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_read_json(path_file: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях"""
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.debug(f"Успешно считан JSON-файл: {path_file}")
                return data
            else:
                logger.warning(f"Файл {path_file} не содержит список. Возвращён пустой список.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path_file}")
        return []
    except JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {path_file}")
        return []
