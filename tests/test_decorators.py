import pytest
from pathlib import Path
from datetime import datetime

from src.decorators import log

date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S').strip()


@pytest.mark.parametrize("arg_1, arg_2, expected_result", [(2, 2, f"{date_now} foo ok"),
                                                           (2, "2",
                                                            f"{date_now} foo error: unsupported operand type(s) for +:"
                                                            " 'int' and 'str' Inputs: (2, '2') {}"),
                                                           (None, None,
                                                            f"{date_now} foo error: unsupported operand type(s) for "
                                                            "+: 'NoneType' and 'NoneType' Inputs: (None, None) {}")
                                                           ])
def test_log_decorator(arg_1, arg_2, expected_result):
    @log("log.txt")
    def foo(x: int, y: int) -> int:
        return x + y

    foo(arg_1, arg_2)

    log_mess = Path(Path.home(), "PycharmProjects", "fintech_app", "data", "log.txt").read_text()
    assert log_mess == expected_result


@pytest.mark.parametrize("arg_1, arg_2, expected_result", [(2, 2, f"{date_now} foo ok"),
                                                           (2, "2",
                                                            f"{date_now} foo error: unsupported operand type(s) for +:"
                                                            " 'int' and 'str' Inputs: (2, '2') {}"),
                                                           (None, None,
                                                            f"{date_now} foo error: unsupported operand type(s) for "
                                                            "+: 'NoneType' and 'NoneType' Inputs: (None, None) {}")
                                                           ])
def test_console_log(capsys, arg_1, arg_2, expected_result):
    @log(None)
    def foo(x: int, y: int) -> int:
        return x + y

    foo(arg_1, arg_2)

    log_mess = capsys.readouterr()

    assert log_mess.out.strip() == expected_result
