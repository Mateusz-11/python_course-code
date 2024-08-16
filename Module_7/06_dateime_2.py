from datetime import datetime

birthday = input('Write birthdate dd.mm.rrrr: ')
d = datetime.strptime(birthday, '%d.%m.%Y')

print(d)