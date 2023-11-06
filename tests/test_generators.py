import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions_list


@pytest.fixture
def get_data():
    return transactions_list


@pytest.fixture
def get_expected_result_filter():
    return [939719570, 142264268, 895315941]


def test_filter_by_currency(get_data, get_expected_result_filter):
    usd_transactions = filter_by_currency(transactions_list, "USD")
    for i in range(3):
        assert next(usd_transactions)["id"] == get_expected_result_filter[i]


@pytest.fixture
def get_expected_result_descriptions():
    return ["Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации"]


def test_transaction_descriptions(get_data, get_expected_result_descriptions):
    descriptions = transaction_descriptions(get_data)
    for i in range(5):
        assert next(descriptions) == get_expected_result_descriptions[i]


@pytest.fixture
def get_get_expected_result_card():
    return [f"0000 0000 0000 000{i}" for i in range(1, 6)]


def test_card_number_generator(get_get_expected_result_card):
    for i, card_number in enumerate(card_number_generator(1, 5)):
        assert card_number == get_get_expected_result_card[i]
