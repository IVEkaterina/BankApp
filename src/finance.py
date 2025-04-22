import csv

import pandas as pd


def read_transactions_from_csv(file_path: str, encoding="utf-8") -> list[dict]:
    """Считывает CSV-файл с финансовыми операциями и возвращает список словарей.

        Аргументы:
            file_path (str): Путь к CSV-файлу.
            encoding (str): Кодировка файла. По умолчанию "utf-8".

        Возвращает:
            list[dict]: Список словарей, каждый из которых представляет одну финансовую операцию.

        Исключения:
            FileNotFoundError: Если указанный файл не найден.
            Exception: Любая другая ошибка при чтении файла.
        """
    try:
        with open(file_path, encoding=encoding) as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except Exception as ex:
        print(f"Произошла ошибка: {ex}")
    return []


print(read_transactions_from_csv("../data/transactions.csv"))


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """Считывает XLSX-файл с финансовыми операциями и возвращает список словарей.

        Аргументы:
            file_path (str): Путь к Excel-файлу (.xlsx).

        Возвращает:
            list[dict]: Список словарей, каждый из которых представляет одну финансовую операцию.

        Исключения:
            UnicodeDecodeError: Ошибка кодировки при чтении файла.
            FileNotFoundError: Если указанный файл не найден.
            Exception: Любая другая ошибка при чтении файла.
        """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except UnicodeDecodeError as ex:
        print(f"Ошибка кодировки: {ex}")
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except Exception as ex:
        print(f"Произошла ошибка: {ex}")
    return []


print(read_transactions_from_excel("../data/transactions_excel.xlsx"))
