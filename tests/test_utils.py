from unittest.mock import patch, mock_open
from src.utils import get_read_json

@patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100}]')
@patch('json.load')
def test_get_read_json(mock_json_load, mock_open):
  mock_json_load.return_value = [{"amount": 100}]
  result = get_read_json("fake_file.json")
  assert result == [{"amount": 100}]
  mock_open.assert_called_once_with("fake_file.json", 'r', encoding='utf-8')
  mock_json_load.assert_called_once()
