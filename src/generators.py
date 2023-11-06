from typing import Generator
from pathlib import Path
import json

transactions_list = json.loads(Path("../data", "transactions.json").read_text())


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """
    Возвращает итератор, который выдает по очереди операции с указанием валюты
    :param transactions: Список словарей транзакция
    :param currency: Поиск по валюте
    :return: Словарь транзакции
    """
    yield from filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == currency, transactions)


usd_transactions = filter_by_currency(transactions_list, "USD")

for _ in range(2):
    print(next(usd_transactions)["id"])


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Возвращает описание каждой операции по очереди
    :param transactions: Список словарей транзакция
    :return: Описание транзакции
    """
    yield from [transaction["description"] for transaction in transactions]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генерирует номера карт в формате "XXXX XXXX XXXX XXXX", где X — цифра
    :param start: Нижний диапазон номеров карт
    :param end: Верхний диапазон номеров карт
    :return: Строку с номером карты
    """

    def get_bank_card(card: int) -> str:
        bank_card = str(card)
        while len(bank_card) != 16:
            bank_card = "0" + bank_card
        return f"{bank_card[:4]} {bank_card[4:8]} {bank_card[8:12]} {bank_card[12:]}"

    yield from list(map(get_bank_card, range(start, end + 1)))
