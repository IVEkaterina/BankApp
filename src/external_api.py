import os
import requests
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv


load_dotenv()


def get_external_api(transaction: List[Dict[str, Any]]) -> Optional[float]:
    if "operationAmount" not in transaction:
        return 0
    else:
        operation_amount = transaction["operationAmount"]
    if "currency" not in operation_amount:
        return 0
    else:
        currency = operation_amount["currency"]
    if "code" not in currency:
        return 0
    else:
        code = currency["code"]
    if "amount" not in operation_amount:
        return 0
    else:
        amount = operation_amount["amount"]

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
    return None