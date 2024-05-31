import random

options = ('paper', 'stone', 'scissors')

gamer_choice = input('>> What is you choice?\n (p) - paper,\n (s) - stone,\n (sc) - scissors\n >> Write here: ')
computer_choice = random.choice(options)

print(f'Gamer choice: {gamer_choice}')
print(f'Computer choice: {computer_choice}')

if gamer_choice == 'p' and computer_choice == 'stone' or gamer_choice == 's' and computer_choice == 'scissors' or gamer_choice == 'sc' and computer_choice == 'paper':
    print('You won!')
elif gamer_choice == 'p' and computer_choice == 'scissors' or gamer_choice == 's' and computer_choice == 'paper' or gamer_choice == 'sc' and computer_choice == 'stone':
    print('Computer won!')
elif gamer_choice == 'p' and computer_choice == 'paper' or gamer_choice == 's' and computer_choice == 'stone' or gamer_choice == 'sc' and computer_choice == 'scissors':
    print('Computer won!')
else:
    print('Incorrect answer. Play again.')
    quit()