import os
from unittest.mock import patch
from src.external_api import get_external_api


@patch('requests.get')
@patch('src.external_api.get_read_json')
def test_get_external_api(mock_get_read_json, mock_requests_get):
    # Мокаем данные, возвращаемые из JSON-файла
    mock_get_read_json.return_value = [
        {
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD"}
            }
        },
        {
            "operationAmount": {
                "amount": "200",
                "currency": {"code": "RUB"}
            }
        }
    ]

    # Мокаем ответ от внешнего API
    mock_requests_get.return_value.json.return_value = {'result': 9500.0}

    # Вызываем функцию и проверяем результат
    result = get_external_api()
    assert result == 9700.0  # 9500 от USD + 200 RUB

    # Проверяем, что запрос был отправлен правильно
    mock_requests_get.assert_called_once_with(
        'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100',
        headers={"apikey": os.getenv('API_KEY')},
        data={}
    )