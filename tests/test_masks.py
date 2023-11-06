import pytest
from src.masks import get_mask_bank_card, get_mask_bank_account


@pytest.fixture
def data_test() -> list[str]:
    return ["1234567890123456", "12345678901234567890"]


def test_get_mask_bank_card(data_test: list[str]) -> None:
    assert get_mask_bank_card(data_test[0]) == "1234 56** **** 3456"
    assert get_mask_bank_card(data_test[1]) == "Введен некорректный номер банковской карты"


def test_get_mask_bank_account(data_test: list[str]) -> None:
    assert get_mask_bank_account(data_test[0]) == "Введен некорректный номер счёта"
    assert get_mask_bank_account(data_test[1]) == "**7890"
