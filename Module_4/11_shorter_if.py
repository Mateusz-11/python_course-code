base = 4000
seniority = int(input('Write seniority in full years: '))
sales = int(input('How many products have you sold? '))
hours = int(input('Hom much time have you worked in last month? '))

seniority_bonus = 0.1 if seniority > 2 else 0.02
sales_bonus = 0.25 if sales > 30 else 0
house_bonus = 0.08 if hours > 160 else 0.02

salary = base + seniority_bonus * base + sales_bonus * base + house_bonus * base

print(f'Full salary: {salary} euro')
