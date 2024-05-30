names = 'Adam Miskiewicz, Adam Asnyk, Zbigniew Nienacki'
list_of_names = names.split(', ')
list_of_first_names = []

for person in list_of_names:
    first_name, second_name = person.split(' ')
    if first_name not in list_of_first_names:
        list_of_first_names.append(first_name)

print(list_of_names)
print(sorted(list_of_first_names, reverse=True))