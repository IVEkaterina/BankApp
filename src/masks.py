def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if card_number.isdigit():
        if len(card_number) == 16:
            card_number = card_number[:6] + "******" + card_number[-4:]
            result = " ".join(card_number[i: i + 4] for i in range(0, 16, 4))
        else:
            result = "Введите 16-значный номер карты"
    else:
        result = "Введите номер карты"
    return result


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if account.isdigit():
        if len(account) == 20:
            account = "**" + str(account[-4:])
        else:
            account = "Введите 20-значный номер счета"
    else:
        account = "Введите номер счета"
    return account