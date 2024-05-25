values = tuple(range(6,1025,6))

print(values)
# 3 first
print(values[:3])
#Amount of numbers
print(f'Amount numbers in values tuple: {len(values)}')

print(values[3::6])
print(values[::-3])
print(f'Average: {sum(values[-10::]) / len(values[-10::])}')
print('- - - - -')
print(values[-10::])