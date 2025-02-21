def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_number = card_number[:6] + "******" + card_number[-4:]
    result = " ".join(card_number[i : i + 4] for i in range(0, 16, 4))

    return result


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account = "**" + str(account[-4:])

    return account
