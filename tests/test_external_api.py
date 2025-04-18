from unittest.mock import Mock, patch
from src.external_api import get_external_api

tran = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}

@patch('src.external_api.requests.get')
@patch('src.external_api.os.getenv')
def test_get_external_api(mock_getenv, mock_requests_get):
    mock_getenv.return_value = 'fake_api_key'
    mock_response = Mock()
    mock_response.json.return_value = {
        "success": True,
        "query": {
            "from": "USD",
            "to": "RUB",
            "amount": 10
        },
        "info": {
            "rate": 95.0
        },
        "result": 950.0
    }
    mock_requests_get.return_value = mock_response
    result = get_external_api(tran)
    assert result == 950.0
    mock_requests_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers = {'apikey': 'fake_api_key'}, data = {})
    mock_getenv.assert_called_once_with('API_KEY')