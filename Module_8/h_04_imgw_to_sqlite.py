import sqlite3
from sys import argv

from requests import get
from datetime import date


def get_weather_for_location(location: str):
    response = get('https://danepubliczne.imgw.pl/api/data/synop')

    for row in response.json():
        if row['stacja'] == location:
            # print(row['stacja'], row['cisnienie'], row['temperatura'])
            # print(f"Nazwa stacji: {row['stacja']}, Temperatura: {row['temperatura']}, Ciśnienie: {row['cisnienie']}")
            return {
                'pressure': row['cisnienie'],
                'temperature': row['temperatura'],
                'station': row['stacja']
            }


def add_weather(connection, created_at: date, weather: dict):
    created_at = created_at.strftime('%Y-%m-%d')
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO weather (created_at, station, temperature, pressure) VALUES(?, ?, ?, ?)', (
            today,
            weather['station'],
            weather['temperature'],
            weather['pressure']
        ))
    connection.commit()


def get_weather_for_date_and_location(connection, created_at: date, location: str) -> dict:
    cursor = connection.cursor()
    result = cursor.execute('''
        SELECT * FROM weather WHERE station =? AND created_at=?''', (location, created_at.strftime('%Y-%m-%d')
                                                                   ))
    return result.fetchone()


def initialize_db(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''CREATE TABLE weather(
            weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            station TEXT,
            temperature REAL,
            pressure REAL)
        ''')


with sqlite3.connect('h_04_weather.db') as connection:
    if len(argv) == 2 and argv[1] == 'setup':
        initialize_db(connection)

    station = "Kielce"
    today = date.today()

    row = get_weather_for_date_and_location(connection, today, station)
    if row is None:
        add_weather(connection, today, get_weather_for_location(station))

# print(get_weather_for_location('Kielce'))
# API
# https://danepubliczne.imgw.pl/pl/apiinfo


# result:
# data_pomiaru
# nazwa stacji
# tempfile
# ciśnienie
