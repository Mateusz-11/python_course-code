from datetime import date

today = date.today()
year = today.year

first_day_of_summer = date(year, 6, 21)

if today > first_day_of_summer:
    first_day_of_summer= date(year + 1, 6, 21)


time_delta = first_day_of_summer - today
print(f'to summer left {time_delta.days} days.')
