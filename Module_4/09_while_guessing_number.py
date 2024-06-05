from random import randint

# Guessing game

random_number = randint(1, 100)

print('Guess the number between 1 and 100')
# print(f'{random_number}')
guessing = True
counter = 1
while guessing:
    print('- - -' * 5)

    hit = int(input(('Your attempt: ')))
    if hit == random_number:
        print('>> You guessed!')
        print(f'You needed: {counter} rounds!')
        break
    elif hit > random_number:
        print('>> Too low')
        print(f'It\'s your: {counter} round!')
        counter += 1
    elif hit < random_number:
        print('>> Too low')
        print(f'It\'s your: {counter} round!')
        counter += 1
    else:
        print('Your answer it isn\'t a number')
        counter += 1
