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
