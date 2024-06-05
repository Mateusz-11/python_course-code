students = {
    ('Piotr', 'Kowalczyk'),
    ('Katarzyna', "Mazur"),
    ('Tomasz', "Adamski"),
    ('Agnieszka', "Kaczmarek"),
    ('Krzysztof', "Krawczyk")
}

going_on_trip = {
    ('Katarzyna', "Mazur"),
    ('Tomasz', "Adamski"),
    ('Krzysztof', "Krawczyk")
}
print(f'Students who left at school: ')
for index, _ in enumerate(students - going_on_trip):
    print(index + 1, _)

# print(f'Students who left at school: {students - going_on_trip}')
