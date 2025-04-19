import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_external_api(transaction: dict) -> float:
    """функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,"""
    code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    amount = transaction.get("operationAmount", {}).get("amount", 0)

    if code == "RUB":
        return float(amount)
    if code in ["USD", "EUR"]:
        try:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

            headers = {
                "apikey": os.getenv('API_KEY')
            }

            response = requests.get(url, headers=headers, data={})

            result = response.json()

            if 'result' in result:
                return result['result']
        except Exception as e:
            print(e)
    return 0
