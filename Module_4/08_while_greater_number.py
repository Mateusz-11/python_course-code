numbers = []
state = True
number = None
while state:
    new_number = int(input('Write number greater than the previous one: '))
    if number is None or new_number > number:
        numbers.append(new_number)
        number = new_number
    else:
        state = False

print(numbers)
print(f'Average of created list of numbers is equal {sum(numbers) / len(numbers)}')
