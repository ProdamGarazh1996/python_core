import json

file_name = "users.json"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        users_data = json.load(file)

    print(f"Успешно загружены данные из файла '{file_name}'\n")

    for index, user in enumerate(users_data, start=1):
        try:
            username = user["username"]
            password = user["password"]
            expected_result = user["expected_result"]

            print(f"Пользователь №{index}:")
            print(f"  Логин: {username}")
            print(f"  Пароль: {password}")
            print(f"  Ожидаемый результат: {expected_result}")
            print("-" * 30)

        except KeyError as e:
            print(f"Ошибка в блоке данных пользователя №{index}: "
                  f"отсутствует обязательное поле {e}")
            print("-" * 30)

except FileNotFoundError as e:
    print(f"Ошибка: Файл '{file_name}' не найден.")
    print(f"Подробности ошибки: {e}")

except json.JSONDecodeError as e:
    print(f"Ошибка: Не удалось прочитать файл '{file_name}'. "
          f"Файл поврежден или имеет неверный формат JSON.")
    print(f"Подробности ошибки: {e}")

except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
