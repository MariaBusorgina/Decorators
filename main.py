import os
from utils import decorator_logger, decorator_logger_path


@decorator_logger
def summa(a, b):
    return a + b


@decorator_logger_path(path)
def myltiply(a, b):
    return a * b


path = os.path.relpath(path='new_file.txt', start=None)
summa(1, 5)
myltiply(2, 5)
