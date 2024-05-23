birth_year = int(input('Text age to test: '))
current_year = 2024

age = current_year - birth_year

print(f'Age of person born in {birth_year} is {age}.')
if age >= 18:
    print('Adult')
else:
    print('Underage')

if birth_year % 4 == 0 and birth_year % 100 != 0 or birth_year % 400 == 0:
    print(f'Year {birth_year} is a leap year')
else:
    print(f'Year {birth_year} is NOT a leap year')