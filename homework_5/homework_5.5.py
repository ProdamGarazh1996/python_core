import json
from functools import reduce


def add(fist_number, second_number):
    return fist_number + second_number


input_file = "test_results.json"
output_file = "test_report.json"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        tests = json.load(file)

    if not isinstance(tests, list):
        raise ValueError("Корневой элемент JSON должен быть списком.")

    valid_statuses = {"PASS", "FAIL", "SKIP"}

    for index, test in enumerate(tests, start=1):
        absent_parameters = []
        if not isinstance(test, dict):
            raise ValueError(f"Элемент №{index} не является словарем.")
        if not ("name" in test):
            absent_parameters.append("name")
        if not ("status" in test):
            absent_parameters.append("status")
        if not ("duration" in test):
            absent_parameters.append("duration")

        if len(absent_parameters) != 0:
            if len(absent_parameters) == 1:
                raise KeyError(
                    f"В элементе №{index} "
                    f"отсутствует обязательное поле {absent_parameters[0]}")
            else:
                raise KeyError(
                    f"В элементе №{index} отсутствуют "
                    f"обязательные поля ({', '.join(absent_parameters)}).")

        if test["status"] not in valid_statuses:
            raise ValueError(
                f"В элементе №{index} "
                f"указан некорректный статус: '{test['status']}'.")
        if (not isinstance(test["duration"], (int, float))
                or test["duration"] < 0):
            raise ValueError(
                f"В элементе №{index} "
                f"указано некорректное время выполнения: {test['duration']}.")

    total_tests = len(tests)

    pass_count = sum(1 for t in tests if t["status"] == "PASS")
    fail_count = sum(1 for t in tests if t["status"] == "FAIL")
    skip_count = sum(1 for t in tests if t["status"] == "SKIP")

    failed_tests = filter(lambda t: t["status"] == "FAIL", tests)
    failed_names = [t['name'] for t in failed_tests]
    durations = [t['duration'] for t in tests]
    total_duration = reduce(add, durations)

    longest_test = max(tests, key=lambda t: t["duration"]) if tests else None
    longest_test_info = {
        "name": longest_test["name"],
        "duration": longest_test["duration"]
    } if longest_test else None

    report = {
        "total_tests": total_tests,
        "metrics": {
            "PASS": pass_count,
            "FAIL": fail_count,
            "SKIP": skip_count
        },
        "failed_test_names": failed_names,
        "longest_test": longest_test_info,
        "total_duration": round(total_duration, 2)
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)

    print(f"Отчет успешно сформирован и сохранен в файл '{output_file}'")

except FileNotFoundError as e:
    print(f"Ошибка: Файл '{input_file}' не найден.")
    print(f"Подробности: {e}")

except json.JSONDecodeError as e:
    print(f"Ошибка: "
          f"Не удалось прочитать файл '{input_file}'. "
          f"Некорректный формат JSON.")
    print(f"Подробности: {e}")

except (KeyError, ValueError) as e:
    print(f"Ошибка структуры данных во входном файле: {e}")

except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
