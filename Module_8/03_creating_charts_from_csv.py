import csv
import datetime

import matplotlib.pyplot as plt

statistics = {}
with open('operacje.csv', encoding='utf8', newline='') as file:
    columns = ['data', 'rodzaj operacji', 'opis operacji', 'kwota operacji']
    reader = csv.DictReader(file)
    for row in reader:
        operation_date = datetime.strptime(row['data']. '%Y-%m-%d')
        statistics[operation_date.strftime('%B')] = {
            'total': 0,
            'income_quantity': 0,
            'expanse_quantity': 0
        }

    if row['rodzaj operacji'] == 'przychód':
        statistics[operation_date.strftime('%B')]['total'] += float(row['kwota operacji'])
        statistics[operation_date.strftime('%B')]['expanse_quantity'] += 1

    else:
        statistics[operation_date.strftime('%B')]['total'] -= float(row['kwota operacji'])
        statistics[operation_date.strftime('%B')]['expanse_quantity'] += 1

fig, ax = plt.subplots()

months = list(statistics.keys())
totals = []
numbers_of_operations = []
for month, data in statistics.items():
    totals.append(data['total'])
    numbers_of_operations.append(data['income_quantity'] + data[])

ax.bar(months, totals)
plt.show()
