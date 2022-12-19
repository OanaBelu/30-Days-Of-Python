# Day 17 - Flexible Functions with *args and **kwargs

"""The problem

Some of you may have noticed that several of the built in functions accept a variable number of arguments.
For example, let's look at good old print.

print can actually take an arbitrary number of positional arguments, and it will print them all side by side
by default:"""

print(1, 2, 3, 4, 5)  # 1 2 3 4 5

"""The character that gets put between these values is controlled by another parameter called sep, which has a default
value of " ". That's why we get a single space between each item."""

print(1, 2, 3, 4, 5, sep=", ")


# Accepting an arbitrary number of positional arguments

def mul(x, y):
    print(x * y)


mul(5, 10)


def mul(*args):
    print(args[0] * args[1])


mul(5, 10)


def multigreet(*args):
    for name in args:
        print(f"Hello , {name}!")


multigreet("Ras", "Carl", "Po", "Fih")


# One thing to be very aware of, is that when we refer to our parameter in the loop, we use the name args, not *args.
# Always remember that this * is an operator.

def multigreet(*names):
    for name in names:
        print(f"Hello, {name}!")


multigreet("Ras", "Carl", "Po", "Fih")


# Parameter order with *args :
# When we use a parameter like *args we have to be very aware of the order of our parameters.
# This is because any parameters we define after the *args cannot accept positional arguments
#
# def multigreet(*names, other):
#     for name in names:
#         print(f"Hello, {name}!")
#
# multigreet("Jose", "Phil")  # TypeError: multigreet() missing 1 required keyword-only argument: 'other'

# If we instead put the other parameter first, this exception goes away

def multigreet(other, *names):
    for name in names:
        print(f"Hello, {name}!")


multigreet("Jose", "Phil")

# print actually makes use of this with sep and end, which only accept keyword arguments

# Accepting an arbitrary number of keyword arguments
dict(name="Phil", age=29, city="Budapest", nationality="British")


def dict_nat(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


dict_nat(name="Phil", age=29, city="Budapest", nationality="British")


# another special parameter : **kwargs, which is short for keyword arguments
def pretty_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


pretty_print(title="The Matrix", director="Wachowski", year=1999)

# title: The Matrix
# director: Wachowski
# year: 1999

# We have access to .items() in there, because kwargs is a dictionary.
# If we define both *args and **kwargs for a given function, **kwargs has to come second.
# If the order is reversed, Python considers it invalid syntax

# Other uses for * and ** : we can also use them for the opposite: unpacking an iterable into individual values.
# we put a * before the iterable we're passing in as an argument
numbers = [1, 2, 3, 4, 5]

print(*numbers, sep=" | ")  # 1 | 2 | 3 | 4 | 5
print(numbers, sep=" | ")  # [1, 2, 3, 4, 5]


def print_movies(*args):
    for value in args:
        print(value)


movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movies(*movie.values())
# The Matrix
# Wachowski
# 1999

print_movies(*movie.keys())


# title
# director
# year

def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_movie(**movie)


# title: The Matrix
# director: Wachowski
# year: 1999

# Here when we do **movie when calling the function, it turns the dictionary into keyword arguments.
# These are passed to print_movie, and the **kwargs parameter collects them back into a dictionary

def print_movie(movie_details):
    for key, value in movie_details.items():
        print(f"{key}: {value}")


movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(movie)


# title: The Matrix
# director: Wachowski
# year: 1999

# And it would be valid, but **kwargs can give us more flexibility when it comes to collecting unassigned keyword
# arguments, and not only those coming from a dictionary
def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(studio="Warner Bros", **movie)


# studio: Warner Bros
# title: The Matrix
# director: Wachowski
# year: 1999

# exemple 1:
def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']})")

    print()


# Instead of using an f-string here, we could use the format method with named placeholders.
# We could then pass in **book to format
def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print("{title}, by {author} ({year})".format(**book))

    print()


# we can define the template elsewhere, which also means we can refer to it in multiple places in our code:
book_template = "{title}, by {author} ({year})"


def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print(book_template.format(**book))

    print()


"""Exercises

1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. 
Remember that we can use the sum function to add the values in an iterable."""

def add(*args):
    print(sum(args))

add(3,0,2,9,11)

"""2) Create a function that accepts any number of positional and keyword arguments, and that prints them back to the 
user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword 
 arguments."""

def arg_pos(*args,**kwargs):
    print(f"Position arguments are: {args}")
    print(f"Keywords arguments are: {kwargs}")

arg_pos(1,  "blue",  [1,  23,  3], height=184, key=lambda x: x ** 2)

def arg_printer(*args, **kwargs):
    args = [str(arg) for arg in args]
    print(f"Positional arguments are: {', '.join(args)}")

arg_printer(1,  "blue",  [1,  23,  3], height=184, key=lambda x: x ** 2)

def arg_printer(*args, **kwargs):
    args = [repr(arg) for arg in args]
    print(f"Positional arguments are: {', '.join(args)}")

    kwargs = [f"{key}={repr(value)}" for key, value in kwargs.items()]
    print(f"Keyword arguments are: {', '.join(kwargs)}")


"""3) Print the following dictionary using the format method and ** unpacking."""

country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

country_template = """Name: {name}
Population: {population}
Capital: {capital}
Currency: {currency}"""

print(country_template.format(**country))


"""4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument 
for print function's sep parameter for this exercise."""
print(*range(1,21), sep =",")

"""5) Modify your code from exercise 4 so that each number prints on a different line. You can only use a 
single print call."""
print(*range(1,21), sep ="\n")