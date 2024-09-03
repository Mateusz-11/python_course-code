# odczyt CSV - zwraca listę
import csv

with open('1_orders.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print(row)

# zapis do CSV
import csv

with open('1_orders.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    writer.writerow([4, 'Peter', 'Smith'])

# odczyt pliku CSV (gdy są nagłówki) - zwraca słownik
import csv

with open('1_orders.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print(row['first_name'], row['last_name'])

# zapis do CSV (z nagłówkami)
import csv

with open('1_orders.csv', mode='w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'first_name': 'Peter', 'last_name': 'Smith'})