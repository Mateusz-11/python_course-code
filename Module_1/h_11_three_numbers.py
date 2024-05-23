a = int(input('Number A: '))
b = int(input('Number B: '))
c = int(input('Number C: '))

max_value = 0
min_value = 0

if a > b:
    if a > c:
        max_value = a
    else:
        max_value = c
else:
    if b > c:
        max_value = b
    else:
        max_value = c

if a < b:
    if a < c:
        min_value = a
    else:
        min_value = c
else:
    if b < c:
        min_value = b
    else:
        min_value = c

print(f'Maximum value = {max_value}')
print(f'Minimum value = {min_value}')
