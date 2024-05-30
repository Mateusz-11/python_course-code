list_of_numbers = []

for i in range(5):
    new_number = int(input(f'Write number {i+1} of 5: '))
    list_of_numbers.append(new_number)

min_value = min(list_of_numbers)
max_value = max(list_of_numbers)
avg_value = sum(list_of_numbers) / len(list_of_numbers)

print(f'All list: {list_of_numbers}')
print(f'Minimum value: {min_value}')
print(f'Maximum value: {max_value}')
print(f'Average value: {avg_value}')
