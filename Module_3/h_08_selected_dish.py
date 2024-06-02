import random

dishes = {
    'soup': ['pomidorowa', 'barszcz', 'rosół'],
    'dinner': ['pulpety', 'schabowy', 'gołąbki'],
    'dessert': ['lody', 'kisiel', 'ciasto'],
}

# raffle of meals

for k, v in dishes.items():
    selected_dish = random.choice(v)
    print(f'Selected {k} is: {selected_dish}')

