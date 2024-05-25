number = int(input('Text number: '))

total = 0
amount_numbers = 0
multiply_result = 1
for counter in range(2, number + 1, 2):
    total += counter
    amount_numbers += 1
    multiply_result *= counter
    print(f'{counter}', end=", ")

print(f'Sum of numbers is equal: {total}')
print(f'Multiply of numbers is equal: {multiply_result}')
print(f'Avarage of these number is equal: {total / amount_numbers}')
