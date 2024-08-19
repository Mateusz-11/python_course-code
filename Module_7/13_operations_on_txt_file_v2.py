with open('13_students_data.txt', encoding='utf8') as input_file, open('13_output_v2.txt', encoding='utf8', mode='w') as output_file:
    for line in input_file:
        first_name, last_name, note = line.strip().split(';')
        if note == '3':
            output_file.write(f'{first_name};{last_name},{note}\n')

