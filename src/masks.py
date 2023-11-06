def get_mask_bank_card(bank_card: str) -> str:
    """
    Вывод маски банковской карты
    :param bank_card: банковская карта
    :return: Маска банковской карты
    """
    if len(bank_card) != 16 or not bank_card.isdigit():
        return "Введен некорректный номер банковской карты"
    else:
        return f"{bank_card[0:4]} {bank_card[4:6]}** **** {bank_card[12:]}"


def get_mask_bank_account(bank_account: str) -> str:
    """
    Вывод маски банковского счета
    :param bank_account: Счет клиента
    :return: Маска счета клиента
    """
    if len(bank_account) != 20 or not bank_account.isdigit():
        return "Введен некорректный номер счёта"
    else:
        return f"**{bank_account[-4:]}"
