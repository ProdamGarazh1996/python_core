from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('название функции: ', func.__name__)
        result = func(*args, **kwargs)
        print('Функция завершилась, результат выполнения: ', result)

    return wrapper


@decorator
def count_number_of_args(*args, **kwargs):
    """Подсчитывает количество всех аргументов"""
    num_args = len(args)
    num_kwargs = len(kwargs)
    return num_args + num_kwargs


count_number_of_args('one', 'two', 'three', g='four')

print("\n--Метаданные--")
print(count_number_of_args.__doc__)
print(count_number_of_args.__name__)
print(count_number_of_args.__annotations__)
