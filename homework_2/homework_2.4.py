attempts_number = 0
secret_number = 37
while True:
    attempts_number = attempts_number + 1
    number_entered = input("Please enter a number: ")
    if number_entered == "" or number_entered.isdigit() is False:
        print("Incorrect Input")
        continue
    else:
        number_entered = int(number_entered)

    if number_entered == secret_number:
        print("Correct! Number of attempts:", attempts_number)
        break
    elif number_entered > secret_number:
        print("secret number is lower")
    else:
        print("secret number is higher")
