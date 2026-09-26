class InvalidTestStatusError(Exception):
    pass


def validate_test_status(status):
    valid_statuses = {"PASS", "FAIL", "SKIP"}
    if status not in valid_statuses:
        raise InvalidTestStatusError(
            f"Недопустимый статус теста: '{status}'. "
            f"Допустимы только: {', '.join(valid_statuses)}.")
    print(f"Статус '{status}' успешно проверен и является корректным.")


test_statuses = ["PASS", "SKIP", "INVALID_STATUS", "FAIL", "READY"]

for status in test_statuses:
    print(f"Проверка статуса: {status}")
    try:
        validate_test_status(status)
    except InvalidTestStatusError as e:
        print(f"Ошибка: {e}")
    print("-" * 50)
