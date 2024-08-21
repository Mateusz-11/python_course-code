with open('14_transactions_data.txt', encoding='utf8') as input_file, open('14_output_incomes.txt', encoding='utf8', mode='w') as output_file:
    for line in input_file:
        date, description, amount = line.strip().split(';')
        if int(amount) > 0:
            output_file.write(f'{date}, {description}, {amount}\n')
