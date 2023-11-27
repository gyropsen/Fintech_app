import logging

logger = logging.getLogger(__name__)


def get_mask_bank_card(bank_card: str) -> str:
    """
    Вывод маски банковской карты
    :param bank_card: банковская карта
    :return: Маска банковской карты
    """
    logger.info("Start get_mask_bank_card")
    if len(bank_card) != 16 or not bank_card.isdigit():
        logger.error("Incorrect bank card number")
        return ""
    else:
        logger.info("get_mask_bank_card successfully")
        return f"{bank_card[0:4]} {bank_card[4:6]}** **** {bank_card[12:]}"


def get_mask_bank_account(bank_account: str) -> str:
    """
    Вывод маски банковского счета
    :param bank_account: Счет клиента
    :return: Маска счета клиента
    """
    logger.info("Start get_mask_bank_account")
    if len(bank_account) != 20 or not bank_account.isdigit():
        logger.error("Invalid account number")
        return ""
    else:
        logger.info("get_mask_bank_account successfully")
        return f"**{bank_account[-4:]}"
