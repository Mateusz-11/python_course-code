names = 'Anna', 'Halina', 'Marta', 'Monika'

test_name = input('Text your name: ')

if test_name in names:
    print(f'Imię {test_name} is in list of names')
else:
    print(f'Imię {test_name} isn`t in list of names')
