from random import choice, sample

# word jumble - pomieszanie słów

# User selects a word from list, and try to guess from jumble words.

list_of_words = ['python', 'javascript', 'java', 'sql', 'php', 'ruby']
selected_word = choice(list_of_words)
shuffle_word = "".join(sample(selected_word, len(selected_word)))

print("Hello in guessing game! \n Below you see jumble word. Guess what it means. \n You have 3 chances!")
print('- - - ' * 5)
print(f'Try to figure out what means that word: "{shuffle_word}"')
print('- - - ' * 5)

for counter in range(3):
# counter of choices
    print(f'You have {3 - counter} chances')
    answer = input(f'>> Write here: ')
# statement of checking answer
    if answer == selected_word:
        print('>> You won!')
        break
    elif answer != selected_word and counter == 2:
        print('- - - ' * 5)
        print('>> You lost! Try again.')
    else:
        print('Wrong answer!')
