import random


def generate_login():
    random_id = random.randint(1000, 9999)
    return f"user_{random_id}"


def generate_age():
    return random.randint(18, 65)


def generate_status():
    statuses = ["ACTIVE", "BLOCKED", "INACTIVE"]
    return random.choice(statuses)


def generate_user():
    return {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status()
    }
