from random import choice

# Asking about capital of country
# With counting points

capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Czechy': 'Praga',
    'Słowacja': 'Bratysława',
    'Ukraina': 'Kijów',
}

points = 0
for _ in range(3):
    print(f'Round: {_ + 1} of 3')
    selected_country = choice(list(capitals.keys()))

    answer = input(f'What is the capital of {selected_country}? ')
    if answer == capitals.get(selected_country):
        points += 1
        print('You guessed!')
    else:
        print('Wrong answer!')
    print('- - ' * 5)

if points == 3:
    print('You\'ve got: 3/3 points')
elif points == 2:
    print('You\'ve got: 2/3 points')
elif points == 1:
    print('You\'ve got: 1/3 points')
elif points == 0:
    print('You\'ve got: 0/3 points')
