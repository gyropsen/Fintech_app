from pathlib import Path
import json
from typing import Any
import logging

logger = logging.getLogger(__name__)


def get_transactions_list(path: str) -> Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path: Путь до JSON-файла
    :return: Список словарей транзакций
    """
    logger.info("Start get_transactions_list")
    try:
        transactions_list = json.loads(
            Path(path).read_text())
        logger.info("get_transactions_list successfully")
        return transactions_list
    except Exception as error:
        logger.error(f"get_transactions_list error: {error}")
        return []


def get_amount_transaction(transaction: dict) -> Any:
    """
    Принимает на вход одну транзакцию и возвращает сумму транзакции в рублях или ошибку ValueError
    :param transaction: Словарь транзакции
    :return: Сумма транзакции
    """
    logger.info("Start get_amount_transaction")
    if not transaction:
        logger.error("get_amount_transaction error: ValueError")
        raise ValueError("Пустой список")

    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("get_amount_transaction successfully")
        return transaction["operationAmount"]["amount"]

    logger.error("get_amount_transaction error: ValueError")
    raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
