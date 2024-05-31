import random

options = ('paper', 'stone', 'scissors')

try:
    gamer_choice = options[
    int(input('>> What is you choice?\n (1) - paper,\n (2) - stone,\n (3) - scissors\n >> Write here: ')) - 1]
except:
    print('Incorrect answer. Play again.')
    quit()

computer_choice = random.choice(options)

print(f'>> Gamer choice: {gamer_choice}')
print(f'>> Computer choice: {computer_choice}')

if gamer_choice == 'paper' and computer_choice == 'stone' or \
        gamer_choice == 'stone' and computer_choice == 'scissors' or \
        gamer_choice == 'scissors' and computer_choice == 'paper':
    print('You won!')
elif gamer_choice == 'paper' and computer_choice == 'scissors' or \
        gamer_choice == 'stone' and computer_choice == 'paper' or \
        gamer_choice == 'scissors' and computer_choice == 'stone':
    print('Computer won!')
else:
    print('We have draw!')
