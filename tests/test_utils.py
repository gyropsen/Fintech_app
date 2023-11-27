import pytest
from pathlib import Path
import json
from unittest.mock import patch

from src.utils import get_amount_transaction, get_transactions_list, read_csv_or_xlsx


@pytest.fixture
def get_data():
    return json.loads(
        Path(Path(__file__).parent.parent, "data", "operations.json").read_text())


def test_get_transactions_list(get_data):
    assert get_data == get_transactions_list(str(Path(Path(__file__).parent.parent, "data", "operations.json")))
    assert [] == get_transactions_list("")
    assert [] == get_transactions_list(str(Path(Path(__file__).parent.parent, "data", "None.json")))
    assert [] == get_transactions_list(str(Path(Path(__file__).parent.parent, "data", "not_list.json")))


def test_get_amount_transaction(get_data):
    assert get_data[0]["operationAmount"]["amount"] == get_amount_transaction(get_data[0])


def test_get_amount_transaction_value_error(get_data):
    with pytest.raises(ValueError) as exinfo:
        get_amount_transaction(get_data[1])

    assert "Транзакция выполнена не в рублях. Укажите транзакцию в рублях" in str(exinfo.value)

    with pytest.raises(ValueError) as exinfo:
        get_amount_transaction(get_transactions_list("/home/egor/PycharmProjects/fintech_app/data/None.json"))

    assert "Пустой список" in str(exinfo.value)


@patch("src.utils.read_csv_or_xlsx")
def test_read_csv_or_xlsx(mock_read_csv_or_xlsx):
    test_dict = {'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                 'operationAmount': {'amount': 16210.0, 'currency': {'name': 'Sol', 'code': 'PEN'}},
                 'description': 'Перевод организации', 'from': 'Счет 58803664561298323391',
                 'to': 'Счет 39745660563456619397'}
    mock_read_csv_or_xlsx.return_value = test_dict
    assert read_csv_or_xlsx("/home/egor/PycharmProjects/fintech_app/data/transactions.csv")[0] == test_dict
