movies = [
    {'title': 'Ojciec Chrzestny', 'director': 'Francis Ford Cappola', 'year': 1972},
    {'title': 'Skazani na Showshank', 'director': 'Frank Darbont', 'year': 1994},
    {'title': 'Szeregowiec Ryan', 'director': 'Steven Spilberg', 'year': 1998},
    {'title': 'Obywatel Kane', 'director': 'Orson Welles', 'year': 1998},
    {'title': 'Casablanka', 'director': 'Michael Curtiz', 'year': 1942},
    {'title': 'Titanic', 'director': 'James Cameron', 'year': 1997},
    {'title': 'Lista Shindlera', 'director': 'Steven Spilberg', 'year': 1993},
]

## delete movies made by Spilberg
# I version
for movie in movies:
    if movie['director'] == 'Steven Spilberg':
        movies.remove(movie)

# print(movies)

# II version
movies_2 = []
for movie in movies:
    if movie['director'] != 'Steven Spilberg':
        movies_2.append(movie)
        print(movie)

print(movies_2)