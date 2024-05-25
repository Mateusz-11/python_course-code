personal_data = ('John', 'Smith', 40)
print(f'Name: {personal_data[0]}')
print(f'Last name: {personal_data[1]}')
print(f'Age: {personal_data[2]}')

print('- - - - - ' * 10)

numbers = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

for i in numbers:
    # print(f'{i[0]} + {i[1]} + {i[2]} = {i[0] + i[1] + i[2]}')
    print(f'{i[0]} + {i[1]} + {i[2]} = {sum(i)}')
