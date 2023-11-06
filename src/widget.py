from datetime import datetime

from src.masks import get_mask_bank_card, get_mask_bank_account


def get_description(description: str) -> str:
    """Вывод описания"""
    information_list = description.split(" ")
    name = " ".join(information_list[:-1])
    numbers = information_list[-1]

    if "счет" == name.lower() or "счёт" in name.lower():
        return f"{name} {get_mask_bank_account(numbers)}"
    else:
        return f"{name} {get_mask_bank_card(numbers)}"


def get_date(string: str) -> str:
    """Преобразование даты в строку"""
    return str(datetime.strftime(datetime.fromisoformat(string), "%d-%m-%Y")).replace("-", ".")
