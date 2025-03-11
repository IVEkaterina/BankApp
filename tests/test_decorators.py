import pytest
from src.decorators import log, my_function

def test_log(capsys):
    with pytest.raises(Exception):
        captured = capsys.readouterr()
        assert captured.out == f"my_function error: {e}. Inputs:{args}, {kwargs}\n"
    @log
    def my_function(x = "6", y = [1, 2, 3]):
        return x + y