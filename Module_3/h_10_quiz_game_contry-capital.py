from random import choice

# Asking about capital of country

capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Czechy': 'Praga',
    'Słowacja': 'Bratysława',
    'Ukraina': 'Kijów',
}

selected_country = choice(list(capitals.keys()))

answer = input(f'What is the capital of {selected_country}? \n >> ')
if answer == capitals.get(selected_country):
    print('You guessed!')
else:
    print('Wrong answer!')
