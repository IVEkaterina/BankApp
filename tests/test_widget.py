import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('value, expected', [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758")
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_mask_account_card_with_not_str():
    with pytest.raises(AttributeError):
        mask_account_card(1)
    with pytest.raises(TypeError):
        mask_account_card()


def test_get_date_with_not_date():
    with pytest.raises(IndexError):
        get_date("")
    with pytest.raises(IndexError):
        get_date("3444474")


@pytest.mark.parametrize('value, expected', [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2008-07-23", "23.07.2008")
])
def test_get_date(value, expected):
    assert get_date(value) == expected
