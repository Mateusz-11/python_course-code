from datetime import date

class Author:
    def __init__(self, first_name: str, last_name: str, date_of_birth: date):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

class Book:
    def __init__(self, title: str, genre: str, description: str, abstract: str, grade: float):
        self.title = title
        self.genre = genre
        self.authors = []
        self.description = description
        self.abstract = abstract
        self.grade = grade

    def add_authors(self, author: Author):
        self.authors.append(author)



author_1 = Author('Bonifacy', 'Smith', date(1910, 10, 10))
author_2 = Author('John', 'Smith', date(1905, 5, 15))

book = Book('Przykładowy tytył', 'Kryminał', 'Opis książki', 'Krótkie strzeszczenie', 5.0)

book.add_authors(author_1)
book.add_authors(author_2)

print(book.title)
print(book.genre)
print(book)
print(book.authors[0].date_of_birth)