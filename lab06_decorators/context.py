from contextlib import contextmanager


@contextmanager
def operation_logger(name):
    print(f"--- Начало операции: {name} ---")
    try:
        yield
    finally:
        print(f"--- Завершение операции: {name} ---")