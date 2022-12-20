# Day 20 - map, filter, and Conditional Comprehensions

# what comprehensions are for:
# We use a comprehension when we want to make a new collection from some other iterable.
# However, there are cases where we want to make a new collection and a comprehension isn't necessary.
# We only use a comprehension when we want to change something about the values when we make this new collection.
# For example, we might want to turn every string in a list to title case
names = ["tom", "richard", "harold"]
names = [name.title() for name in names]
print(names)
# If we just want to turn the names list to, say, a set, we can do this instead
names = set(names)
print(names)
# We don't have to bother with a much more verbose set comprehension
names = {name for name in names}
print(names)


# With this in mind, we can really think of comprehensions as a way of performing an action for every item in some
# iterable, and then storing the results

# The map function : map is a function that allows us to call some other function on every item in an iterable
# map is a way of performing some action for every item in an iterable, just like a comprehension
# Let's say I want to cube every number in a list of numbers. We can use map like so:
def cube(number):
    return number ** 3


numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)


# map objects are another lazy type, like the things we get back from calling zip, enumerate, or range.
# map doesn't actually bother calculating any values until we ask for them
# This allows map to be a lot more memory efficient than the comprehensions we've looked at so far, because it
# doesn't have to store all the values at once
# So how can we get things out of a map object? Well, they're iterable, so we can iterate over the values :

def cube(number):
    return number ** 3


numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

for number in cubed_numbers:
    print(number)


# Since they're iterable, we can also unpack them using *:
def cube(number):
    return number ** 3


numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

print(*cubed_numbers, sep=", ")


# We can also convert them to a normal collection if we like:
def cube(number):
    return number ** 3


numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube, numbers))
print(*cubed_numbers, sep=", ")


# One of the really nice things about map is that is can handle several iterables at once
# This means the function gets called with multiple arguments. The order of those arguments matches the order in which
# we passed the iterables to map
def add(a, b):
    return a + b


odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

# we can recreate the cube example above using a lambda expression like so:
numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(lambda number: number ** 3, numbers)

# We could have used a lambda expression here like this:
totals = map(lambda a, b: a + b, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

# operator has an add function ready to go, so we don't have to define it ourselves
from operator import add

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 22]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 31

# methodcaller allows us to easily define a function that calls a method for us. We just have to provide the method
# name as a string.
from operator import methodcaller

names = ["tom", "richard", "harold"]
title_names = map(methodcaller("title"), names)

# a lambda expression approach :
names = ["tom", "richard", "harold"]
title_names = map(lambda name: name.title(), names)

# Conditional comprehensions: We do this by providing a condition at the end of our comprehension, and this condition
# determines whether or not an item makes it into our new collection. In cases where the condition evaluates to True,
# the item is added; otherwise, it gets discarded.

# For example, let's say we have a set of numbers and I only want the even values. We can use a conditional
# comprehension to accomplish this
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# This comprehension is equivalent to writing a for loop like this:
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# We can do this filtering operation with any kind of comprehension, so we could do the same thing for a set
# comprehension, for example
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = {number for number in numbers if number % 2 == 0}

# The filter function : Much like map is a functional analogue for "normal" comprehensions,
# filter performs the same role as a conditional comprehension

# Much like map, filter calls a function (known as a predicate) for every item in an iterable, and it discards any
# values for which that function returns a falsy value.
# A predicate is a function that accepts some value as an argument and returns either True or False.

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(lambda number: number % 2 == 0, numbers)

# In this case we don't have an easy solution available in the operator module—though there is a mod function—so
# we have to either use a lambda expression, or we have to define a function to call.

# In this case, I think it's worth defining a little helper function, because it makes things a lot more readable
def is_even(number):
    return number % 2 == 0

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(is_even, numbers)

# Just like map, filter gives us a lazy filter object, so the values are not calculated until we need them
# However, unlike map, the filter function can only handle a single iterable at a time

# Instead of passing in a function to filter, it's possible to use the value None
values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ")  # Hello, 435, -4.2

# example:
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

# example :
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

# with map :
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

# example:
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)

# with map:
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)

"""Exercises

1) Use map to call the strip method on each string in the following list:
Print the lines of the nursery rhyme on different lines in the console.

Remember that you can use the operator module and the methodcaller function instead of a lambda expression if you 
want to."""

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]

def line_stripper(line):
    return line.strip()

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]

print(*map(line_stripper, humpty_dumpty), sep="\n")

# with lambda
print(*map(lambda line: line.strip(), humpty_dumpty), sep="\n")

# with methodcaller
from operator import methodcaller

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]

print(*map(methodcaller("strip"), humpty_dumpty), sep="\n")


"""2) Below you'll find a tuple containing several names:

Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new 
list. Make sure that every name in the new list is in title case."""

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single,
# readable line
name_comprehension = [name.title() for name in names if len(name) < 8]
print(name_comprehension)

"""3) Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to 
the console."""

print(*filter(lambda number: number >= 0, range(-5, 11)))

#  I think it makes a lot of sense to create a separate function for our filter predicate:
def is_positive(number):
    return number >= 0

print(*filter(is_positive, range(-5, 11)))







