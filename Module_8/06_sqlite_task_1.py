import sqlite3
from sys import argv
def setup():
    with sqlite3.connect('books.db') as connection:
        sql = '''CREATE TABLE books(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100) UNIQUE NOT NULL,
            author VARCHAR(100)
        )'''

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

# umożliwia tworzenie nowej tabeli po wywyłaniu programu: python3 06_sqlite_task_1.py setup
if len(argv) ==2 and argv[1] == 'setup':
    setup()


with sqlite3.connect('books.db') as connection:
    cursor = connection.cursor()
    for book in cursor.execute('SELECT book_id, title, author FROM  books'):
        print(book)

    title = input('Podaj tytuł: ')
    author = input('Podaj imię i nazwisko autora: ')

    cursor.execute(
        'INSERT INTO books(title, author) VALUES(?, ?)',
    (title, author)
    )
    connection.commit()
