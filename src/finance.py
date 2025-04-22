import pandas as pd
import csv

def read_transactions_from_csv(file_path: str, encoding="utf-8") -> list[dict]:
    """Читает CSV-файл с финансовыми операциями и возвращает список словарей."""
    try:
        with open(file_path, encoding=encoding) as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except Exception as ex:
        print(f"Произошла ошибка: {ex}")
        return []

print(read_transactions_from_csv("../data/transactions.csv"))


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """Считывает финансовые операции из XLSX-файла и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except UnicodeDecodeError as ex:
        print(f"Ошибка кодировки: {ex}")
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except Exception as ex:
        print(f"Произошла ошибка: {ex}")

print(read_transactions_from_excel("../data/transactions_excel.xlsx"))