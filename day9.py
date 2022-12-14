
# Day 9 - Unpacking, Enumeration, and the zip Function

# Unpacking :
# Unpacking is generally used to perform several assignments at once, by extracting the individual values from some
# iterable. This process is also called destructuring
# movie = ("12 Angry Men", "Sidney Lumet", 1957)
#
# title = movie[0]
# director = movie[1]
# year = movie[2]
#
# movie = ("12 Angry Men", "Sidney Lumet", 1957)
#
# title, director, year = movie

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
    print(f"{movie[0]} ({movie[2]}), by {movie[1]}")
for title, director, year in movies:
    print(f"{title} ({year}), by {director}")

# Enumeration: One common application for unpacking is when using a function called enumerate
for index in range(len(movies)):
    print(f"{index + 1}. {movies[index][0]} ({movies[index][2]}), by {movies[index][1]}")

counter = 1

for title, director, year in movies:
    print(f"{counter}. {title} ({year}), by {director}")
    counter += 1

names = ["Harry", "Rachel", "Brian"]

for counter, name in enumerate(names, start=1):
    print(f"{counter}. {name}")

for counter, movie in enumerate(movies, start=1):
    print(f"{counter}. {movie[0]} ({movie[2]}), by {movie[1]}")

