with open('numbers.txt', 'r') as f:
    number_array = []
    for line in f:
        number_array.extend(line.split())
    if len(number_array) < 4:
        print('error! There must be at least 4 numbers')
    else:
        print(number_array[0])
        print(number_array[1])
        print(number_array[len(number_array) - 2])
        print(number_array[len(number_array) - 1])
