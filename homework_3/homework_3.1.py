from collections import Counter


def get_test_statistics(entered_value):
    entered_value = Counter(entered_value)
    if "PASS" not in entered_value:
        entered_value["PASS"] = 0
    if "SKIP" not in entered_value:
        entered_value["SKIP"] = 0
    if "FAIL" not in entered_value:
        entered_value["FAIL"] = 0

    return dict(entered_value)


while True:
    value_entered = input("Enter the statuses of tests: ")
    if value_entered == "":
        print("value is empty")
        continue
    else:
        break

statuses = value_entered.split()
statuses = [
    status for status in statuses
    if status == 'PASS' or status == 'SKIP' or status == 'FAIL'
]
test_statistics = get_test_statistics(statuses)
for key, value in test_statistics.items():
    print(f"{key}: {value}")
total_count = sum(test_statistics.values())
print(f"Successful: {((test_statistics['PASS'] / total_count) * 100):.1f}%")
