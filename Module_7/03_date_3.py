from datetime import date

today = date.today()
next_birthday = date(today.year, 2, 1)

if next_birthday < today:
    next_birthday = date(today.year + 1, 2, 1)

diff = next_birthday - today
age = today - next_birthday

print(f"Your next birthday date: {next_birthday.strftime('%a, %d.%m.%Y')}")
print(f"{diff} days left until your birthday")