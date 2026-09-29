numbers_string = ''
with open('numbers.txt', 'r') as f:
    number_array = []
    for line in f:
        number_array.extend(line.split())
    number_array = list(map(lambda x: int(x) ** 2, number_array))
    numbers_string = ' '.join(str(x) for x in number_array)
with open('numbers.txt', 'w') as f:
    f.write(numbers_string)
