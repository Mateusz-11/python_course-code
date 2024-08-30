from json import load, dump

new_author = 'Witold Gombrowicz'
new_title = "Ferdydurke"

with open('15_books.json') as file:
    # it generate string
    # print(file.read())

    # it generate list
    # print(load(file))

    books = load(file)

with open('15_books.json', "w") as file:
    books.append({
        'title': new_title,
        'author': new_author
    })
    dump(books, file)

for book in books:
    print("Title: ", book.get('title'))
    print("Author: ", book.get('author'))
    print("- - - " * 5)