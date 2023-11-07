import pytest
from pathlib import Path
import json

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def get_data() -> list[dict]:
    transactions = json.loads(
        Path(Path.home(), "PycharmProjects", "fintech_app", "data", "transactions.json").read_text())
    return transactions


@pytest.fixture
def get_expected_result_filter() -> list[int]:
    return [939719570, 142264268, 895315941]


@pytest.fixture
def get_expected_result_descriptions() -> list[str]:
    return ["Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации"]


@pytest.fixture
def get_expected_result_card() -> list[str]:
    def get_bank_card(card: int) -> str:
        bank_card = str(card)
        while len(bank_card) != 16:
            bank_card = "0" + bank_card
        return f"{bank_card[:4]} {bank_card[4:8]} {bank_card[8:12]} {bank_card[12:]}"

    return list(map(get_bank_card, range(1, 6)))


def test_filter_by_currency(get_data: list[dict], get_expected_result_filter: list[int]) -> None:
    usd_transactions = filter_by_currency(get_data, "USD")
    for i in range(3):
        assert next(usd_transactions)["id"] == get_expected_result_filter[i]


def test_transaction_descriptions(get_data: list[dict], get_expected_result_descriptions: list[str]) -> None:
    descriptions = transaction_descriptions(get_data)
    for i in range(5):
        assert next(descriptions) == get_expected_result_descriptions[i]


def test_card_number_generator(get_expected_result_card: list[str]) -> None:
    for i, card_number in enumerate(card_number_generator(1, 5)):
        assert card_number == get_expected_result_card[i]
