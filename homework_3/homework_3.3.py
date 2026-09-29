import random

TESTS = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]


def get_valid_count(max_count):
    while True:
        try:
            prompt = f"Enter the number of tests to run (1-{max_count}): "
            count = int(input(prompt))
            if count > max_count:
                print(
                    f"Error: Cannot run {count} tests. "
                    f"Only {max_count} are available."
                )
                continue
            if count < 0:
                print("Error: Number of tests cannot be negative.")
                continue
            return count
        except ValueError:
            print("Error: Please enter a valid integer.")


def generate_test_results(tests_list, count):
    statuses_pool = ["PASS", "FAIL", "SKIP"]
    selected_tests = random.sample(tests_list, count)
    generated_statuses = [random.choice(statuses_pool) for _ in range(count)]
    return selected_tests, generated_statuses


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


def main():
    count = get_valid_count(len(TESTS))
    if count is None:
        return

    selected_tests, generated_statuses = generate_test_results(TESTS, count)
    print_report(selected_tests, generated_statuses)


if __name__ == "__main__":
    main()
