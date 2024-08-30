from json import load

new_author = 'Witold Gombrowicz'
new_title = "Ferdydurke"

with open('15_books.json') as file:
    # it generate string
    # print(file.read())

    # it generate list
    # print(load(file))

    books = load(file)

for book in books:
    print("Title: ", book.get('title'))
    print("Author: ", book.get('author'))
    print("- - - " * 5)
