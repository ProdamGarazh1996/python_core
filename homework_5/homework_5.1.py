from functools import reduce


def failed_tests(test):
    if test["status"] == "FAIL":
        return True
    else:
        return False

def add(fist_number, second_number):
    return fist_number + second_number

tests = [
    {"name": "test_login", "status": "PASS", "duration": 1.5},
    {"name": "test_register", "status": "FAIL", "duration": 2.3},
    {"name": "test_logout", "status": "PASS", "duration": 0.8},
    {"name": "test_payment", "status": "FAIL", "duration": 4.1},
    {"name": "test_profile", "status": "SKIP", "duration": 0.3},
    {"name": "test_settings", "status": "PASS", "duration": 1.2},
]

failed_tests = filter(failed_tests, tests)
failed_titles = list(map(lambda t: t["name"], failed_tests))
durations = [t['duration'] for t in tests]
total_duration = reduce(add, durations)

passed_titles = [t["name"] for t in tests if t["status"] == "PASS"]
pass_count = sum(1 for t in tests if t["status"] == "PASS")
fail_count = sum(1 for t in tests if t["status"] == "FAIL")
skip_count = sum(1 for t in tests if t["status"] == "SKIP")

print("--- Статистика тестов ---")
print(f"Количество PASS: {pass_count}")
print(f"Количество FAIL: {fail_count}")
print(f"Количество SKIP: {skip_count}")
print(f"Список упавших тестов (FAIL): {failed_titles}")
print(f"Список успешных тестов (PASS): {passed_titles}")
print(f"Общее время выполнения всех тестов: {total_duration} сек.")
