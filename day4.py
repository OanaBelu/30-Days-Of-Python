# Day 4 - Basic Python Collections

# Lists :
# names = ["John", "Alice", "Sarah", "George"]
# movie_titles = [
#     "Eternal Sunshine of the Spotless Mind",
#     "Memento",
#     "Requiem for a Dream"
# # ]
# friend_details = ["John", 27, "Web Developer"]
# It’s also possible to define a list with no content, which is represented by an empty pair of square brackets []
# Each value in a list is indexed according to its position in the list
# It’s also possible to refer to a negative index, which allows us to work from the end of the list
# Adding items to a list using the append method
# names = ["John", "Alice", "Sarah", "George"]
# names.append("Simon")
# We can also add another item (or items) to a list using the + operator. In this case, both operands must be lists
# names = ["John", "Alice", "Sarah", "George"]
# names = names + ["Simon"]
# If we want to add an item in the middle we have the insert method.First we need to tell it where we want to
# insert the value, and second we need to tell it what we want to insert.
# numbers = [1, 2, 4, 5]
# numbers.insert(2, 3)
# print(numbers)  # [1, 2, 3, 4, 5]

# Removing items from a list : remove method -  it removes the first item that matches the value we pass in
# names = ["John", "Sarah", "Alice", "John"]
# names.remove("John")
#
# print(names)  # ['Sarah', 'Alice', 'John']
# Sometimes we don’t necessarily know the value we want to remove, but we know where the value is in our list
# we can use the del keyword
# names = ["John", "Sarah", "Alice", "Mike"]
# del names[0]
#
# print(names)  # ['Sarah', 'Alice', 'Mike']
# The main alternative we have to using del is pop. By default pop is going to remove the last item in the list,
# but we can optionally pass in an index as an argument to remove a different item instead.
# names = ["John", "Sarah", "Alice", "Mike"]
# names.pop()
# print(names)  # ['John', 'Sarah', 'Alice']
#
# names.pop(1)
# print(names)  # ['John', 'Alice']

# names = ["John", "Sarah", "Alice", "Mike"]
# last_in_line = names.pop()
#
# print(names)         # ['John', 'Sarah', 'Alice']
# print(last_in_line)  # Mike

# clear: This one is pretty straightforward, it’s just going to remove everything inside a given list
# names = ["John", "Sarah", "Alice", "John"]
# names.clear()
#
# print(names)  # []

# Tuples :
# Much of the time, these parentheses are optional—it’s the commas that are important
# names = "John", "Sarah", "Alice"
# names = ("John", "Sarah", "Alice")
# movies = [
#     ("Eternal Sunshine of the Spotless Mind", 2004),
#     ("Memento", 2000),
#     ("Requiem for a Dream", 2000)
# ]

# Tuples vs lists :
# One of big differences between tuples and lists is that tuples are immutable
# This means you won’t find any pop or append methods for tuples, and the del keyword isn’t going to allow
# you to remove values using an index

# Accessing values in nested collections :
# movies = [
#     ("Eternal Sunshine of the Spotless Mind", 2004),
#     ("Memento", 2000),
#     ("Requiem for a Dream", 2000)
# ]
# movies[0][0]  # "Eternal Sunshine of the Spotless Mind"

"""Exercises

    1. Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name,
    the release year of the movie, and the movie’s budget.
    2. Use the input function to gather information about another movie. You need a title, director’s name, release
    year, and budget.
    3. Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple
    you wrote in the movies list.
    4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
    5. Add the new movie tuple to the movies collection using append.
    6. Print both movies in the movies collection.
    7. Remove the first movie from movies. Use any method you like.
"""

# 1. Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name,
#    the release year of the movie, and the movie’s budget

# movies = [("Avatar", "James Francis Cameron", "2009", "$237 millions")]

# 2. Use the input function to gather information about another movie. You need a title, director’s name, release
#    year, and budget
# title = input("Title: ")
# director = input("Director's name: ")
# year = input("Year of release: ")
# budget = input("Budget: ")

# 3. Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple
#     you wrote in the movies list
# movies = [("Avatar", "James Francis Cameron", "2009", "$237 millions")]
# title = input("Title: ")
# director = input("Director's name: ")
# year = input("Year of release: ")
# budget = input("Budget: ")
#
# new_movies = title, director, year, budget


# 4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
# print(f'{title} {year}')
# print(f'{new_movies[0]} ({new_movies[2]})')

# 5. Add the new movie tuple to the movies collection using append
movies = [("Avatar", "James Francis Cameron", "2009", "$237 millions")]
title = input("Title: ")
director = input("Director's name: ")
year = input("Year of release: ")
budget = input("Budget: ")

new_movies = title, director, year, budget

print(f'{new_movies[0]} ({new_movies[2]})')

movies.append(new_movies)
print(movies)

#     6. Print both movies in the movies collection.
print(movies[0])
print(movies[1])

#     7. Remove the first movie from movies. Use any method you like.
movies.remove(movies[0])
