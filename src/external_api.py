import os
import requests
from dotenv import load_dotenv
from src.utils import get_read_json

load_dotenv()


def get_external_api() -> float:
    tran = get_read_json('../data/operations.json')
    counter = 0

    for transaction in tran:
        if "operationAmount" not in transaction:
            continue
        operation_amount = transaction["operationAmount"]
        if "currency" not in operation_amount:
            continue
        currency = operation_amount["currency"]
        if "code" not in currency:
            continue
        code = currency["code"]
        if "amount" not in operation_amount:
            continue
        amount = operation_amount["amount"]

        if code == "RUB":
            counter += float(amount)
        if code in ["USD", "EUR"]:
            try:
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

                headers = {
                    "apikey": os.getenv('API_KEY')
                }

                response = requests.get(url, headers=headers, data={})

                result = response.json()

                for res in result:
                    if 'result' not in res:
                        continue
                    resultation = result['result']
                    counter += resultation

            except Exception as e:
                print(e)

    return counter
