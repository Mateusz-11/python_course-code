import requests


def get_authors_slug(author_name: str) -> str:
    request = requests.get('http://wolnelektury.pl/api/authors/')
    for author in request.json():
        if author_name == author['name']:
            return author['slug']


author_slug = get_authors_slug(input('Wrtie name and surname of author: '))

if author_slug is not None:
    request = requests.get(f"http://wolnelektury.pl/api/authors/{author_slug}/books")
    for book in request.json():
        print(book.get('title'))