# show name of month which depends by number
# 1 == January

# solution with match case
number = int(input('Write number of month: '))

match number:
    case 1:
        print(f'{number} is January')
    case 2:
        print(f'{number} is February')
    case 3:
        print(f'{number} is March')
    case 4:
        print(f'{number} is April')
    case 5:
        print(f'{number} is May')
    case 6:
        print(f'{number} is June')
    case 7:
        print(f'{number} is July')
    case 8:
        print(f'{number} is August')
    case 9:
        print(f'{number} is September')
    case 10:
        print(f'{number} is October')
    case 11:
        print(f'{number} is November')
    case 12:
        print(f'{number} is December')
    case _:
        print(f'{number} doesn\'t exist')

# solution with dictionary
# number = int(input('Write number of month: '))
#
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
#           9: 'September', 10: 'October', 11: 'November', 12: 'December', }
#
# print(f'{number} is {months.get(number, "not exist")}')
