users = list(range(1, 21))

for user in users:
    if user == 18:
        print("Testing aborted")
        break
    else:
        if user == 5 or user == 10 or user == 15:
            continue
        else:
            print("Testing lunched for user:", user)
