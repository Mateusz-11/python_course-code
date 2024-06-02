from random import shuffle

# 52 karty
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

# colors in ascii
colors = [chr(9824), chr(9827), chr(9829), chr(9830)]
values = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
cards = []

for color in colors:
    for value in values:
        cards.append(f'{value}{color}')

# print(cards)
# print('- - - ')

for counter in range(26):
    print(f'Round: {counter + 1}')
    shuffle(cards)
    print(f'Cards drawn: {cards[:2]}')
    cards.pop(0)
    cards.pop(0)
    print(f'Remaining cards: {cards}')
    print('- - - ' * 5)
