import csv

mydict = [
    {'name': 'Hennessey Venom F5', 'time_to_100': '2.6', 'speed_record': '484'},
    {'name': 'SSC Tuatara', 'time_to_100': '2.5', 'speed_record': '460'},
    {'name': 'Koenigsegg AAgera RS', 'time_to_100': '3.1', 'speed_record': '457'},
    {'name': 'Koenigsegg One 1', 'time_to_100': '2.6', 'speed_record': '450'},
]

fields = [
    'Name', 'time_to_100', 'speed_record'
]

with open('04_fast_cars.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
