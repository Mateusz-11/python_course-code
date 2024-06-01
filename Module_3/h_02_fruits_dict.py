fruits = {
    'bananas': 8,
    'apples': 6,
    'oranges': 4,
    'kivies': 15
}

## I version

# price apples
print(fruits['apples'])
# price bananas
print(fruits['bananas'])

## II version

for fruit in fruits:
    if fruit in ('bananas', 'apples'):
        print(f'Price of {fruit} is: {fruits[fruit]}')
