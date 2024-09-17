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
        for task in cursor.execute('SELECT * FROM todos WHERE is_done=0'):
            print(task)

        title = input('Co masz do zrobienia? ')

        cursor.execute(
            'INSERT INTO todos(title) VALUES (?)', (title,))
        connection.commit()

def change_status():
    with sqlite3.connect('07_todo_list.db') as connection:
        cursor = connection.cursor()
        for task in cursor.execute('SELECT * FROM todos WHERE is_done=0'):
            print(task)

        id_task = int(input('Napisz ID zadania, które zrobiłeś: '))
        cursor.execute(
            'UPDATE todos SET is_done=1 WHERE todo_id=?', (id_task,)
        )
i = 1
while i == 1:
    print("- - - - - - - - - - - - - - \n "
          "Co chcesz teraz zrobić? \n "
          "0 - Dodaj nowe zadanie \n "
          "1 - Ustaw zadanie jako zrealizowane \n "
          "2 - Zamknij program\n ")
    choice = int(input('Twój wybór: '))
    match choice:
        case 0:
            adding_task()
        case 1:
            change_status()
        case 2:
            break
        case _:
            print('Nieprawidłowy wybór')
            break
