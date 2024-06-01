animals = {
    'pies': 4,
    'kot': 4,
    'krowa': 4,
    'świnia': 4,
    'kurczak': 2,
    'konik polny': 4,
    'żaba': 4,
    'pająk': 8,
    'mrówka': 6,
    'ślimak': 0
}

## finding animal with the smallest number of legs
# tmp_numbers = []
# for animal in animals:
#     tmp_numbers.append(animals[animal])
#
# min_number = min(tmp_numbers)

min_number = None
for animal in animals:
    if min_number is None or animals[animal] < min_number:
        min_number = animals[animal]

for k, v in animals.items():
    if v == min_number:
        print(f'Animal with the smallest number of legs (on that list) is: {k} - {v} legs')
