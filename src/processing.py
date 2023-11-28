import re
from collections import Counter
from typing import Any


def get_dicts_by_key(dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Возвращает список словарей, полученных по ключу состояния
    :param dicts: исходный список словарей
    :param state: ключ состояние
    :return: Избранный список словарей
    """
    return [i for i in dicts if i["state"] == state]


def get_dicts_sort_by_date(dicts: list[dict], reverse: bool = True) -> list[dict]:
    """
    Принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты
    :param dicts: список словарей
    :param reverse: Порядок сортировки
    :return: Список отсортированных словарей
    """
    return sorted(dicts, key=lambda x: x["date"], reverse=reverse)


def search_description(transactions_list: list[dict], pattern: Any) -> list[dict]:
    pattern = re.compile(pattern)
    return [transaction for transaction in transactions_list if pattern.search(transaction['description'])]


def get_statistics_category(transactions_list: list[dict]) -> dict:
    counted = Counter(transaction['description'] for transaction in transactions_list)
    return dict(counted)
