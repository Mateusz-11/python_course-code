# 1 task

numbers = (1, 2, 3, 4, 5, 4, 3, 2, 1, 20, 25)

# for number in numbers:
#     if number % 4 == 0 or number % 5 == 0:
#         print(number)

# task 2

names = 'Piotr', 'Michał', 'Adam', 'Dariusz', 'Antek'

# for name in names:
#     if len(name) > 5:
#         print(name)

# task 3

for counter in reversed(range(1,5)):
    # print(counter)
    for counter2 in range(1,counter+1):
        print(counter2, end=' ')
    print()