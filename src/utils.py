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


def get_list_transactions(not_formatted_list: list[dict]) -> list[dict]:
    list_transactions = []
    for transaction in not_formatted_list:
        list_transactions.append({'id': transaction['id'],
                                  'state': transaction['state'],
                                  'date': transaction['date'],
                                  'operationAmount': {'amount': transaction['amount'],
                                                      'currency': {'name': transaction['currency_name'],
                                                                   'code': transaction['currency_code']}},
                                  'description': transaction['description'],
                                  'from': transaction['from'],
                                  'to': transaction['to']})
    logger.info("read_csv_or_xlsx successfully")
    return list_transactions


def read_csv_or_xlsx(path: str) -> Any:
    """
    Чтение финансовых операций с CSV- и XLSX-файлов
    :param path: Путь до файла
    :return: dataframe
    """
    logger.info("Start read_csv_or_xlsx")

    try:
        if ".csv" in path:
            return get_list_transactions(pd.read_csv(path, delimiter=";").to_dict("records"))
        else:
            return get_list_transactions(pd.read_excel(path).to_dict("records"))
    except Exception as error:
        logger.error(f"read_csv_or_xlsx error: {error}")
        return error
