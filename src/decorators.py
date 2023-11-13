from pathlib import Path
from datetime import datetime
from functools import wraps
from typing import Callable, Any


def log(filename: None | str) -> Callable:
    """
    Логирует вызов функции и ее результат в файл или в консоль
    :param filename: Название файла с логами
    :return: None
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> None:
            if not filename:
                try:
                    func(*args, **kwargs)
                    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} ok")
                except Exception as error:
                    print(
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} "
                        f"error: {error} Inputs: {args} {kwargs}")

            else:
                data_result = Path(Path.home(), "PycharmProjects", "fintech_app", "data", filename)
                try:
                    func(*args, **kwargs)
                    data_result.write_text(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} ok")
                except Exception as error:
                    data_result.write_text(
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} "
                        f"error: {error} Inputs: {args} {kwargs}")

        return inner

    return wrapper


@log(filename="log.txt")
def my_function(x: int | float, y: int | float) -> int | float:
    """Возвращает сумму аргументов"""
    return x + y


my_function(2, 2)
