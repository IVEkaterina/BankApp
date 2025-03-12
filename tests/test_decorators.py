import pytest

from src.decorators import addition, division, multiplication, subtraction


def test_addition(capsys):
    addition(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "addition ok\n"


def test_division(capsys):
    with pytest.raises(ZeroDivisionError):
        division(2, 0)
    captured = capsys.readouterr()
    assert "division error: ZeroDivisionError. Inputs: (2, 0), {}\n" in captured.out


def test_multiplication():
    multiplication(2, 3)
    with open("mylog.txt", "r") as file:
        lines = file.readlines()
        assert lines[-1] == "multiplication ok\n"


def test_subtraction():
    with pytest.raises(TypeError):
        subtraction("a", 1)
    with open("error.txt", "r") as file:
        lines = file.readlines()
        assert "subtraction error: TypeError. Inputs: ('a', 1), {}" in lines[-1]
