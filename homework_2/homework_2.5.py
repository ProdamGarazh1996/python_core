from collections import Counter

tests_count = 0
statuses = []
while True:
    tests_count = input("Please enter number of tests: ")
    if tests_count == "" or tests_count.isdigit() is False:
        print("Incorrect Input")
    else:
        tests_count = int(tests_count)
        break

while True:
    status_entered = input(f"Enter the status of test #{len(statuses) + 1}: ")
    if (status_entered == ""
            or (status_entered != "PASS"
                and status_entered != "FAIL"
                and status_entered != "SKIP")):
        print("Incorrect status!")
        continue
    statuses.append(status_entered)
    if len(statuses) == tests_count:
        break

statistics = Counter(statuses)
message = None
if "PASS" not in statistics:
    statistics["PASS"] = 0
if "SKIP" not in statistics:
    statistics["SKIP"] = 0
if "FAIL" not in statistics:
    statistics["FAIL"] = 0
    message = "Tests run is successful"
else:
    message = "Some tests failed"

print(message)
for key, value in statistics.items():
    print(f"{key}: {value}")
print(f"Successful: {((statistics['PASS'] / tests_count) * 100):.1f}%")
