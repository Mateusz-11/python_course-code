import csv

data = [
    {'Name': 'Hennessey Venom F5', 'time_to_100': 2.6, 'speed_record': 484},
    {'Name': 'SSC Tuatara', 'time_to_100': 2.5, 'speed_record': 460},
    {'Name': 'Koenigsegg Agera RS', 'time_to_100': 3.1, 'speed_record': 457},
    {'Name': 'Koenigsegg One 1', 'time_to_100': 2.6, 'speed_record': 450},
]

columns = [
    'Name', 'time_to_100', 'speed_record'
]

with open('04_fast_cars.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
