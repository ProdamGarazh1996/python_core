correct_password = "Python123"
number = 0
while True:
    if number == 3:
        print("Access Denied")
        break
    entered_password = input("Please enter your password: ")
    if entered_password == correct_password:
        print("Authorization successful")
        break
    else:
        print("Incorrect Password")
    number = number + 1
