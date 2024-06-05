output = []
while len(output) + 1 <= 10:
    try:
        number = int(input(f'Write positive number {len(output) + 1} of 10: '))
    except:
        print('Wrong answer! Try again.')
        number = int(input(f'Write positive number {len(output) + 1} of 10: '))
    if number > 0:
        output.append(number)
    print(output)
    print('- - -' * 5)

print(output)
print('- - - ' * 5)
print(f'Maximum number: {max(output)}')
print(f'Minimum number: {min(output)}')
