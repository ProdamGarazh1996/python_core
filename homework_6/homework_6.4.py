from functools import wraps
import random


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка №{attempt}")
                result = func(*args, **kwargs)
                if result is True:
                    return True
            return False

        return wrapper

    return decorator


@retry(count=5)
def connect_to_server(host, port, secure=True):
    success = random.choice([True, False, False, False, False, False])
    print(f" Подключение к {host}:{port} (secure={secure}) -> "
          f"{'Успешно' if success else 'Ошибка'}")
    return success


print("--- Старт операции ---")
final_result = connect_to_server("192.168.1.1", 8080, secure=False)
print(f"--- Итог: {final_result} ---")
