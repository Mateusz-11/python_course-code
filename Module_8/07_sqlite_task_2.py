import sqlite3
from sys import argv


def setup():
    with sqlite3.connect('07_todo_list.db') as connection:
        sql = '''
            CREATE TABLE todos(
            todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100) UNIQUE NOT NULL,
            is_done INTEGER DEFAULT 0)
        '''

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()


if len(argv) == 2 and argv[1] == 'setup':
    setup()


def adding_task():
    with sqlite3.connect('07_todo_list.db') as connection:
        cursor = connection.cursor()
        for task in cursor.execute('SELECT todo_id, title, is_done FROM todos'):
            print(task)

        title = input('Co masz do zrobienia? ')

        cursor.execute(
            'INSERT INTO todos(title, is_done) VALUES(?, ?)',
            (title, 0)

        )
        connection.commit()

i = 1
while i == 1:
    print("Co chcesz teraz zrobić? \n "
          "0 - Dodaj nowe zadanie \n "
          "1 - Ustaw zadanie jako zrealizowane \n "
          "2 - Zamknij program\n ")
    choice = int(input('Twój wybór: '))
    match choice:
        case 0:
            adding_task()
        case 1:
            continue
        case 2:
            break
