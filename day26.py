# Day 26 - Leveraging the Standard Library

# The namedtuple function - namedtuple is a function available to us in the collections module that gives us the
# ability to define special tuples with named fields

# These special tuples provide awesome readability improvements, because we can retrieve values using the specified
# field names, much like how we use dictionary keys.

# We can also create instances of these tuples using keyword arguments, which allows us to give context to the data
# when populating a tuple with data

# In order to make use of these special tuples, we first need to define templates that specify a name for a given tuple
# configuration, and details the tuple's fields. This is where the namedtuple function comes in. namedtuple is used to
# create this template.

from collections import namedtuple

Book = namedtuple("Book", ["title", "author", "year"])

book = Book("The Colour of Magic", "Terry Pratchett", 1983)
print(f"{book.title} ({book.year}), by {book.author}")

# Python code to demonstrate namedtuple() and
# _make(), _asdict() and "**" operator
# Python code to demonstrate namedtuple() and
# _make(), _asdict() and "**" operator

# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is : ")
print(S._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is : ")
print(Student(**di))


# The partial function : The partial function is a way to create a new version of a function, where some portion of the
# arguments are already given
def exponentiate(base, exponent):
    return base ** exponent


# It's pretty annoying having to write out exponentiate(5, 2) when we could be writing something like square(5).
# It's also less readable.
# While we could go ahead and write another function like this:
def square(base):
    return base ** 2


from functools import partial


def exponentiate(base, exponent):
    return base ** exponent


square = partial(exponentiate, exponent=2)
cube = partial(exponentiate, exponent=3)

print(square(4))  # 16
print(cube(5))  # 125

# The defaultdict type ;The collections module has a few special types of dictionaries for us to work with. The
# defaultdict type is a dictionary that lets us specify some default value to return when we attempt to access a
# key which doesn't exist.

from collections import namedtuple

User = namedtuple("User", ["name", "username", "location"])

users = {
    "0001": User("Phil", "pbest", "Hungary"),
    "0002": User("Jose", "jslvtr", "Scotland"),
    "0003": User("Luka", "lukamiliv", "Serbia")
}

user_id = input("Please enter a user id: ")
user = users.get(user_id)

if user:
    print(user)
else:
    print("Could not find a user matching that user id.")

# Now let's rewrite this using a defaultdict

from collections import defaultdict, namedtuple

User = namedtuple("User", ["name", "username", "location"])

users = defaultdict(
    lambda: "Could not find a user matching that user id.",
    {
        "0001": User("Phil", "pbest", "Hungary"),
        "0002": User("Jose", "jslvtr", "Scotland"),
        "0003": User("Luka", "lukamiliv", "Serbia")

    }
)

user_id = input("Please enter a user id: ")
print(users[user_id])

# we're trying to keep track of an inventory for a character in an RPG of some kind. We're using a dictionary to store
# what is in the character's inventory, with the keys being the item names, and the values being a count of how many
# of this item the character has.
# I'm also going to create a function which is going to modify this dictionary, allowing the user to add new items
inventory = {}


def add_item(item, amount):
    if inventory.get(item):
        inventory[item] += amount
    else:
        inventory[item] = amount


add_item("bow", 1)
add_item("arrow", 20)
add_item("arrow", 20)
add_item("bracer", 2)

print(inventory)  # {'bow': 1, 'arrow': 40, 'bracer': 2}

# This works, but we can do a better job by using a defaultdict with int as the factory function.
from collections import defaultdict

inventory = defaultdict(int)


def add_item(item, amount):
    inventory[item] += amount


add_item("bow", 1)
add_item("arrow", 20)
add_item("arrow", 20)
add_item("bracer", 2)

print(inventory)  # defaultdict(<class 'int'>, {'bow': 1, 'arrow': 40, 'bracer': 2})

"""Exercises

1) Define a Movie tuple using namedtuple that accepts a title, a director, a release year, and a budget. Prompt 
the user to provide information for each of these fields and create an instance of the Movie tuple you defined."""

from collections import namedtuple

Movie = namedtuple("Movie", ["title", "director", "year", "budget"])

title = input("What is the title of the movie? : ")
director = input(f"Who is the director of the movie {title}? : ")
year = input(f"What is the release year for the movie {title}? : ")
budget = input(f"What was the budget for {title}? ")

movie = Movie(title, director, year, budget)

"""2) Use a defaultdict to store a count for each character that appears in a given string. Print the most common 
character in this dictionary."""

from collections import defaultdict

s = input("Please enter a word: ")
letter_count = defaultdict(int)
for char in s:
    letter_count[char] += 1

most_common_char = max(letter_count, key=lambda key: letter_count[key])

print(f"The character ({most_common_char}) appears the most in the word ({s}).")

"""3) Use the mul function in the operator module to create a partial called double that always provides 2 as the 
first argument."""
from operator import mul
from functools import partial

double = partial(mul, 2)
"""4) Create a read function using a partial that opens a file in read ("r") mode."""
from functools import partial

read = partial(open, mode="r")
