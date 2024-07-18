# Number of odds and even numbers on 2 lists

odds = []
even = []

while True:
    number = int(input('Write positive number ("0" - will end the program): '))
    if number == 0:
        break
    elif number % 2 == 0:
        even.append(number)
    else:
        odds.append(number)

print('- - - ' * 6)
print(f'Odds numbers: {odds}')
print(f'Numbers of odds numbers: {len(odds)}')
print('- - - ' * 6)
print('- - - ' * 6)
print(f'Evens numbers: {even}')
print(f'Numbers of evens numbers: {len(even)}')
