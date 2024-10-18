from datetime import datetime

with open("03_data.txt") as file:
    data = file.readlines()

# print(data)

output = []
for row in data:
    # print(row.strip().split(','))
    name, last_name, date_of_birth = row.strip().split(',')
    # print(name)
    # print(name,last_name,date_of_birth)
    date_of_birth = datetime.strptime(date_of_birth, "%d.%m.%Y").strftime('%Y-%m-%d')
    # print(name,last_name,date_of_birth)
    output.append((name, last_name, date_of_birth))

# print(output)

with open("03_output.txt", "w") as output_file:
    for line in output:
        output_file.write(','.join(line) + '\n')