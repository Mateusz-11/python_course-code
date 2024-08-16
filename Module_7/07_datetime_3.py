from datetime import datetime, timedelta

start_date  = datetime.strptime(input('Write start date of work dd.mm.rrrr: '), '%d.%m.%Y')
end_date = datetime.strptime(input('Write end date of work dd.mm.rrrr: '), '%d.%m.%Y')

salary_per_day = int(input('Write your salary per day: '))

full_salary = salary_per_day * ((end_date-start_date).days +1)

while start_date <= end_date:
    if start_date.strftime('%a') in ['Sat', 'Sun']:
        full_salary += salary_per_day
    print(start_date.strftime('%a %d.%m.%Y'))
    start_date += timedelta(days=1)
print(f"You will earn: {full_salary} EUR")

