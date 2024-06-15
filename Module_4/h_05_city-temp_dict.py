data = {}

while True:
    print('- - ' * 5)
    city = input('Write name of city: ')
    temp = float(input('Write temperature (in Celsius degree): '))
    data[city] = temp
    print('- - ' * 5)
    status = input('If you finished, write "End". To continue press Enter: ')
    if status.lower() == "end":
        break

temperatures = []
for k, v in data.items():
    temperatures.append(v)

min_temp = min(temperatures)
max_temp = max(temperatures)
print('- - ' * 5)

print(f'Average temperature is: {sum(temperatures) / len(temperatures)}')

for k, v in data.items():
    if v == min_temp:
        print(f'Minimal temperature ({min_temp}) was in {k}')
    if v == max_temp:
        print(f'Maximum temperature ({max_temp}) was in {k}')
