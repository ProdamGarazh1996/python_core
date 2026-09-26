def check_number_of_tries(number_of_tries, timeout):
    if (number_of_tries < 0 or number_of_tries > 5) and timeout <= 0:
        raise ValueError(
            f"Введенные вами значения {number_of_tries} и {timeout} неверные, "
            f"параметр number_of_tries должен быть в диапазоне от 0 до 5, "
            f"параметр timeout должен быть положительным числом")
    elif number_of_tries < 0 or number_of_tries > 5:
        raise ValueError(
            f"Введенное вами значение {number_of_tries} неверное, "
            f"параметр number_of_tries должен быть в диапазоне от 0 до 5")
    elif timeout <= 0:
        raise ValueError(
            f"Введенное вами значение {timeout} неверное, "
            f"параметр timeout должен быть положительным числом")


test_cases = [
    {"retries": 3, "timeout": 2.5, "description": "Корректные значения"},
    {"retries": 2, "timeout": -1.0, "description": "Отрицательный таймаут"},
    {"retries": 8,
     "timeout": 1.5,
     "description": "Слишком большое количество повторных запусков"}
]

for case in test_cases:
    print(f"Тест: {case['description']}")
    try:
        check_number_of_tries(case["retries"], case["timeout"])
    except ValueError as e:
        print(f"Перехвачено исключение: {e}")
    print("-" * 50)
