numbers = list(range(1, 31))

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("BugTest")
    elif number % 5 == 0:
        print("Test")
    elif number % 3 == 0:
        print("Bug")
    else:
        print(number)
