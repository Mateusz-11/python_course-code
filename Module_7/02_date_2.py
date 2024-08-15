from datetime import date

today = date.today()
day = date(today.year, 11, 9)
formatted = day.strftime("%d.%m.%Y")
print(f"Day of my birthday in this year: {day}")
