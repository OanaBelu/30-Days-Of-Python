
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

for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}. {title} ({year}), by {director}")

# The zip function :used to combined two or more iterables into a single iterable
pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

pets_and_owners = zip(pet_owners, pets)
print(list(pets_and_owners))  # [('Paul', 'Fluffy'), ('Andrea', 'Bubbles'), ('Marta', 'Captain Catsworth')]

for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")

# A caveat for when using enumerate and zip

movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

movies = zip(movie_titles, movie_directors)
for title, director in movies:
    print(f"{title} by {director}.")

movies_list = list(movies)

print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")

# If you try to iterate over movies after the initial loop, you'll also find that it contains no values.
# The reason that this happens is because zip and enumerate produce something called an iterator
# An easy way to bypass this limitation is to just convert the iterator to a non-iterator collection, like a list or
# tuple

movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

movies = list(zip(movie_titles, movie_directors))

"""Exercises

1) Below is some simple data about characters from BoJack Horseman: 
The data contains the character name, the voice actor or actress who plays them, and the species of the character.

Write a for loop that uses destructuring so that you can print each tuple in the following format:

BoJack Horseman is a horse voiced by Will Arnet.

Note that you're going to have to change the species information to lowercase when you print it. If you need a reminder 
on how to do this, we covered it in day 3 of the first week."""

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for character, actor, species in main_characters :
    print(f'{character} is a {species.lower()} voiced by {actor}')


"""2) Unpack the following tuple into 4 variables:
("John Smith", 11743, ("Computer Science", "Mathematics"))
The data represents a student's name, their student id number, and their major and minor disciplines in that order."""

name,id_number,(major_discipline,minor_discipline) = ("John Smith", 11743, ("Computer Science", "Mathematics"))

# Or :
student = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name, id_number, (major, minor) = student

"""3) Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list 
containing three items, and a tuples containing four items."""
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]

print(list(zip(letters, numbers))) # [('a', 1), ('b', 2), ('c', 3)]
