total = 0
while True:
    if (value := int(input('Write an integer: '))) == 0:
        print('End of program')
        print(f'>> Sum of all added numbers: {total}')
        break
    else:
        total += value
        print(f'>> Sum of all added numbers: {total}')
