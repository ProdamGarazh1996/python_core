with open('numbers.txt', 'r') as f:
    number_array = []
    for line in f:
        number_array.extend(line.split())
    odd_numbers = [number for number in number_array if int(number) % 2 != 0]
    even_numbers = [number for number in number_array if int(number) % 2 == 0]
    if len(odd_numbers) > 0:
        with open("odd_numbers.txt", "w") as odd_numbers_file:
            odd_numbers_file.write(' '.join(odd_numbers))
    else:
        with open("odd_numbers.txt", "w"):
            pass
    if len(even_numbers) > 0:
        with open("even_numbers.txt", "w") as even_numbers_file:
            even_numbers_file.write(' '.join(even_numbers))
    else:
        with open("even_numbers.txt", "w"):
            pass
