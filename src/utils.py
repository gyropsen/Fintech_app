from pathlib import Path
import json
from typing import Any


def get_transactions_list(path: str) -> Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path: Путь до JSON-файла
    :return: Список словарей транзакций
    """
    try:
        transactions_list = json.loads(
            Path(path).read_text())
        return transactions_list
    except Exception as error:
        print(error)
        return []


def get_amount_transaction(transaction: dict) -> Any:
    """
    Принимает на вход одну транзакцию и возвращает сумму транзакции в рублях или ошибку ValueError
    :param transaction: Словарь транзакции
    :return: Сумма транзакции
    """
    if not transaction:
        raise ValueError("Пустой список")
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]

    raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
