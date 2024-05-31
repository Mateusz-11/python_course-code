from math import sqrt, pow, ceil, floor
from random import randint

random_number = randint(1, 100)

print(f'Power of {random_number} is: {pow(random_number, 2)}')
print(f'Square of {random_number} is: {ceil(sqrt(random_number))} (rounded up), {floor(sqrt(random_number))} (rounded down)')
