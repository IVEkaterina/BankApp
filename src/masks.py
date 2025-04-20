import logging

logger = logging.getLogger('__name__')
file_handler = logging.FileHandler('../logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if card_number.isdigit():
        if len(card_number) == 16:
            logger.debug(f"Успешно введен номер карты: {card_number}")
            card_number = card_number[:6] + "******" + card_number[-4:]
            result = " ".join(card_number[i: i + 4] for i in range(0, 16, 4))
        else:
            logger.warning(f"Введен не 16-значный номер карты: {card_number}")
            result = "Введите 16-значный номер карты"
    else:
        logger.warning(f"Что-то не так с введенным номером карты: {card_number}")
        result = "Введите номер карты"
    return result


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if account.isdigit():
        if len(account) == 20:
            logger.debug(f"Успешно введен номер счета: {account}")
            account = "**" + str(account[-4:])
        else:
            logger.warning(f"Введен не 20-значный номер счета: {account}")
            account = "Введите 20-значный номер счета"
    else:
        logger.warning(f"Что-то не так с номером : {account}")
        account = "Введите номер счета"
    return account
