test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]


def print_report(test_cases, statuses):
    test_report = zip(test_cases, statuses)
    successful_test_count = 0
    failed_status = False
    for test_case, status in test_report:
        if status == "PASS":
            successful_test_count += 1
        elif status == "FAIL":
            failed_status = True
        print(f"{test_case} - {status}")
    print(f"Successful tests count: {successful_test_count}")
    print(f"Unsuccessful tests count: {len(statuses) - successful_test_count}")
    if failed_status:
        print("test run is failed")
    else:
        print("test run is passed")


print_report(test_cases, statuses)
