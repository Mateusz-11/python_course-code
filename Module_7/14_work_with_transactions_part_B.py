total = 0

with open('14_output_incomes.txt', encoding='utf8') as income_file:
    for line in income_file:
        _, _, amount = line.strip().split(',')
        total += int(amount)

print(f'Total amount from this file is equal to: {total}')