from typing import final

test_list = [1, 12, 23, 34, 5, 3, 21, 55, 22, 100]
chosen_number = int(input('What number you choose? '))

try:
    print(test_list[chosen_number])
except IndexError:
    print("This number doesn't exist")
finally:
    print('here more')