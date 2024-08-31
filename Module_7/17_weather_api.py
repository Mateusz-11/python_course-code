from requests import get

response = get('https://danepubliczne.imgw.pl/api/data/synop')

for row in response.json():
    if row['stacja'] == "Gdańsk" or row['stacja'] == 'Kielce':
        print(row['stacja'], row['cisnienie'], row['temperatura'])