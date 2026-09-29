import test_data


def get_valid_count():
    while True:
        try:
            count = int(input("Enter the number of test users to generate: "))
            if count < 0:
                print("Error: Number of users cannot be negative.")
                continue
            return count
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    count = get_valid_count()
    if count == 0:
        print("No users generated.")
        return

    users = [test_data.generate_user() for _ in range(count)]

    print("\nGENERATED USERS")
    for user in users:
        print(
            f"Login: {user['login']} | "
            f"Age: {user['age']} | "
            f"Status: {user['status']}"
        )

    statuses = [user["status"] for user in users]
    active_count = statuses.count("ACTIVE")
    blocked_count = statuses.count("BLOCKED")
    inactive_count = statuses.count("INACTIVE")

    print("\nSTATUS STATISTICS")
    print(f"ACTIVE: {active_count}")
    print(f"BLOCKED: {blocked_count}")
    print(f"INACTIVE: {inactive_count}")


if __name__ == "__main__":
    main()
