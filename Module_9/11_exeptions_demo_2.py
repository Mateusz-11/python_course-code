dict_demo = {
    'color': 'red',
    'year': 1990,
    'brand': 'VW'
}

# print(dict_demo['color'])
try:
    dict_demo['owner']
except KeyError as message:
    print(message)
    print("Error: This key doesn't exist")