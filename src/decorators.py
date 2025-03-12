from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Any:
    """Декоратор, который логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""

    def decorator(func: Callable[..., Any]) -> Any:
        """Декоратор, логирования начала и конеца выполнения функции, а также ее результаты или возникшие ошибки."""

        @wraps(func)
        def wrapper(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
            """Обертка декоратора"""
            try:
                result = func(*args, **kwargs)
                finish_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(finish_message + '\n')
                else:
                    print(finish_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(error_message + "\n")
                else:
                    print(error_message)
                raise e

        return wrapper

    return decorator


@log()
def addition(x: int, y: int) -> int:
    return x + y


@log(filename="mylog.txt")
def multiplication(m: int, n: int) -> int:
    return m * n


@log()
def division(a, b):
    return a / b


@log(filename="error.txt")
def subtraction(c, d):
    return c - d
