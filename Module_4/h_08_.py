products = {
    'doniczka': 15,
    'konewka': 20,
    'grabie': 12,
    'szpadel': 18,
    'kosiarka': 350,
    'łopata': 22,
    'siekiera': 28,
    'młotek': 12,
    'wiadro': 8,
}

for name, price in products.items():
    print(f"- {name}, price: {price} zł")
print('- - - ' * 5)

cart = {}

while True:
    print('Your cart:')
    basket_sum = 0
    for name, quantity in cart.items():
        print(f"- {name} - {quantity}")
        basket_sum += 4

    print('- - - ' * 4)
    print(f'Cart value: {basket_sum}')
    print('- - - ' * 4)

    status = input('If you want to finish, write "End". To continue press Enter: ')
    if status.lower() == "end":
        break
    print('- - - ' * 4)
    choice = input('What you want to buy? ')
    cart[choice] = cart.get(choice,0) + int(input('How many the product you want to buy? '))



