import pytest

from src.widget import get_description, get_date


@pytest.mark.parametrize("name_numbers, expected_result", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                           ("Счет 64686473678894779589", "Счет **9589"),
                                                           ("Visa Classic 6831982476737658",
                                                            "Visa Classic 6831 98** **** 7658"),
                                                           ("Счет 73654108430135874305", "Счет **4305")
                                                           ])
def test_get_description(name_numbers, expected_result):
    assert get_description(name_numbers) == expected_result


def test_get_date():
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"
