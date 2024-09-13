import sqlite3

## option 1
# connection = sqlite3.connect('library.db')
# connection.close()

## option 2 - context manager
# with sqlite3.connect('library.db') as connection:
#     ...

## select in db
with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    books = cursor.execute('SELECT book_id, title, author FROM books')

    for book in books:
        print(book)

## adding values
with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    title = input('Tytuł: ')
    author = input('Autor: ')
    cursor.execute('INSERT INTO books VALUES (null, ?, ?)', (title, author))
    connection.commit()


