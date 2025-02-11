from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(text: str) -> str:
    new_text = text.split()
    if new_text[0] == "Счет":
        last = get_mask_account(new_text[-1])
    else:
        last = get_mask_card_number(new_text[-1])
    del new_text[-1]
    return " ".join(new_text) + " " + last


def get_date(date: str) -> str:
    new_date = date.split("-")
    day = (new_date[2])[0:2]
    result = [day, new_date[1], new_date[0]]
    return ".".join(result)
