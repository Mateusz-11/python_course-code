import csv

with open('04_fast_cars.csv', newline='', mode='r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        # print(row['Name'], row['time_to_100'], row['speed_record'])
        print(row)