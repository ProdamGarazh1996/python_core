from collections import Counter


def get_test_statistics(results):
    results = Counter(results)
    if "PASS" not in results:
        results["PASS"] = 0
    if "SKIP" not in results:
        results["SKIP"] = 0
    if "FAIL" not in results:
        results["FAIL"] = 0

    return dict(results)


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
total_count = sum(test_statistics.values())
for key, value in test_statistics.items():
    print(f"{key}: {value}")
passed_percentage = 0
if total_count != 0:
    passed_percentage = ((test_statistics['PASS'] / total_count) * 100)
print(f"Successful: {passed_percentage:.1f}%")
