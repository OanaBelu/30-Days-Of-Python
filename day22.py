# Day 22 - Iterators

# An iterable is really any value we can iterate over with something like a for loop
# We can also destructure iterables, and we can create collections from them by passing the value to functions
# like list or tuple

""" Here are some of the iterable types we've encountered so far:

    strings
    lists
    tuples
    dictionaries
    sets
    range objects
    zip objects
    enumerate objects
    map objects
    filter objects """

# an iterable is really just a thing we can get values out of one at a time
# If iterables are the things we can get values out of, iterators are the things which give us those values.
# They're the mechanism Python uses to extract values from iterables.
# Iterators have several important and useful properties that we should be aware of :
# 1. Iterators are often lazy :
# -Being lazy comes with some significant memory benefits, because we only have to keep
# the most recent value in memory
# -it's often not possible to determine the length of a lazy type, because the number
# of items it contains may become apparent only after calculating those values
from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)
for word in a_words:
    print(word)

print(words)

a_words = list(a_words)
print(a_words)  # []

# let's try to grab the first word in our words list that begins with "a"
from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

first_word = next(a_words)
print(first_word)  # "anaconda"
print(next(a_words))  # "anime"
print(next(a_words))  # "addition"
# print(next(a_words)) # StopIteration


"""Exercises

1) Below you'll find a list containing several tuples full of numbers:"""

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
# Solution:
# First things first, lets create our map object. In this case we don't need anything complicated like a
# lambda expression or something from the operator module: we can just use the sum function.
numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
totals = map(sum, numbers)

"""2) Use the map function to find the sum of the numbers in each tuple. Use manual iteration to print the first two 
results provided by the resulting map object."""

# Now that we have a map object assigned to totals, we just need to pass this map object to next to get an item out
# of it. This is possible because map objects are iterators.

print(next(totals))  # 82
print(next(totals))  # 1186
# print(next(totals))  # 603
# print(next(totals))  # 47
# print(next(totals))  # 259

"""3) Imagine you have 3 employees and it's been agreed that the employees will take it in turns to lock up the shop at 
night. This means that for employees A, B, and C, employee A will close the shop on day 1, then B will close the shop 
on day 2, C will close the shop on day 3, and then we start the cycle again with employee A.

Write a program to create a schedule that lists which of your employees will lock up the shop on a given day over 
a 30 day period. You should list the day number, the employee name, and the day of the week. You can choose any 
employee to lock the shop on day 1, and you can also choose which day of the week day 1 corresponds to.

You should make use of the cycle function in the itertools module to create a repeating series of values"""


def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


import itertools

employees = itertools.cycle(["A", "B", "C"])
days = itertools.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

for day_number in range(1, 31):
    print(f"Day {day_number} ({next(days)}): {next(employees)} closes.")
