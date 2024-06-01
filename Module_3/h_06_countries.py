countries = [
    {'country': 'Polska', 'capital': 'Warszawa', 'official_language': 'polski'},
    {'country': 'Niemcy', 'capital': 'Berlin', 'official_language': 'niemiecki'},
    {'country': 'Czechy', 'capital': 'Praga', 'official_language': 'czeski'},
    {'country': 'Słowacja', 'capital': 'Bratysława', 'official_language': 'słowacki'},
]

# Adding one next element (dictionary) to list
countries.append({
    'country': input('Write name country: '),
    'capital': input('Write name capital: '),
    'official_language': input('Write name official_language: ')
})

# Showing all elements in list
for country in countries:
    for k, v in country.items():
        print(f'{k}: {v}')
    print('- - - ' * 5)
