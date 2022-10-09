from datetime import datetime

# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции,
# аргументы, с которыми вызвалась и возвращаемое значение.


def decorator_logger(some_function):
    def new_function(*args, **kwargs):
        now = datetime.now()

        # вызываем some_function
        result = some_function(*args, **kwargs)

        with open('itog.txt', 'w', encoding='utf-8') as file:
            file.write(f"Дата - {now.date()}\n"
                       f"Время - {now.time()}\n"
                       f"Имя функции - {some_function.__name__}\n"
                       f"Аргументы - {args}, {kwargs}\n"
                       f"Результат - {result}")

        # возвращаем результат
        return result

    return new_function

# 2. Написать декоратор из п.1, но с параметром – путь к логам.


def decorator_logger_path(path_logg):
    def decorator_logg(some_function):
        def new_function(*args, **kwargs):
            now = datetime.now()

            # вызываем some_function
            result = some_function(*args, **kwargs)

            with open(f"{path_logg}", 'w', encoding='utf-8') as file:
                file.write(f"Дата - {now.date()}\n"
                           f"Время - {now.time()}\n"
                           f"Имя функции - {some_function.__name__}\n"
                           f"Аргументы - {args}, {kwargs}\n"
                           f"Результат - {result}")

            # возвращаем результат
            return result

        return new_function

    return decorator_logg

