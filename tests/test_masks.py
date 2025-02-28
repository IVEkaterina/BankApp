import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('value, expected', [
  ("7000792289606361","7000 79** **** 6361"),
  ("djjyfo","Введите номер карты"),
  ("12345","Введите 16-значный номер карты"),
  ("87yyg87","Введите номер карты"),
  ("","Введите номер карты")
])

def test_get_mask_card_number(value, expected):
  assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('val, exp', [
  ("73654108430135874305", "**4305"),
  ("fghae", "Введите номер счета"),
  ("21445", "Введите 20-значный номер счета"),
  ("4j56o564h", "Введите номер счета"),
  ("", "Введите номер счета")
])

def test_get_mask_account(val, exp):
  assert get_mask_account(val) == exp
