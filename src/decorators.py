from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Any:
    """Декоратор, который логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""
    def decorator(func: Callable[..., Any]) -> Any:
        """Декоратор, логирования начала и конеца выполнения функции, а также ее результаты или возникшие ошибки."""
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обертка декоратора"""
            start_message = f"{func.__name__} ok"
            if filename:
                with open(filename, "a") as file:
                    file.write(start_message + "/n")
            else:
                print(start_message)
            try:
                result = func(*args, **kwargs)
                finish_message = f"Конец функции {func.__name__} c результам: {result}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(finish_message + "/n")
                else:
                    print(finish_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: ({args}), {{kwargs}}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message + "/n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
