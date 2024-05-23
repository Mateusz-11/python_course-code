# Write program which show information  whether number is divided by 5, 11 or 5 and 11.

test_number = int(input('Text the number: '))

if test_number % 5 == 0 and test_number % 11 == 0:
    print(f'The number {test_number} is divide by 5 and 11')
elif test_number % 5 == 0:
    print(f'The number {test_number} is divide by 5')
elif test_number % 11 == 0:
    print(f'The number {test_number} is divide by 11')
else:
    print(f'The number {test_number} is not divide by 5 or 11')
