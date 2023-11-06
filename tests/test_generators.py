import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions_list


@pytest.fixture
def get_data() -> list[dict]:
    return transactions_list


@pytest.fixture
def get_expected_result_filter() -> list[int]:
    return [939719570, 142264268, 895315941]


def test_filter_by_currency(get_data: list[dict], get_expected_result_filter: list[int]) -> None:
    usd_transactions = filter_by_currency(transactions_list, "USD")
    for i in range(3):
        assert next(usd_transactions)["id"] == get_expected_result_filter[i]


@pytest.fixture
def get_expected_result_descriptions() -> list[str]:
    return ["Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации"]


def test_transaction_descriptions(get_data: list[dict], get_expected_result_descriptions: list[str]) -> None:
    descriptions = transaction_descriptions(get_data)
    for i in range(5):
        assert next(descriptions) == get_expected_result_descriptions[i]


@pytest.fixture
def get_get_expected_result_card() -> list[str]:
    return [f"0000 0000 0000 000{i}" for i in range(1, 6)]


def test_card_number_generator(get_get_expected_result_card: list[str]) -> None:
    for i, card_number in enumerate(card_number_generator(1, 5)):
        assert card_number == get_get_expected_result_card[i]
