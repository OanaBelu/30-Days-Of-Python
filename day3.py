
# Day 3 - Formatting Strings and Processing User Input

# String concatenation -in Python, we can just use the + operator for this (is only supported between strings)
# When using the format method, the placeholders for our values are curly braces, which look like this: {}
# print("Oana is 24 years old!")
# print("{} is {} years old!".format("Oana", 25))
#
# output = "{} is {} years old, and {} works as a {}."
# print(output.format("Oana", 26, "Oana", "test engineer"))

# String interpolation with f-strings
# name = "Oana"
# age = 27
#
# print("{} is {} years old!".format(name, age))

# f-strings are also expressions, so we can assign them to names, or we can print them if we want
# name = "Oana"
# age = 28
#
# print(f"{name} is {age * 12} months old!")

# Basic String Processing - lower, upper, capitalize, and title
# print("Hello, World!".lower())       # "hello, world!"
# print("Hello, World!".upper())     # "HELLO, WORLD!"
# print("Hello, World!".capitalize())  # "Hello, world!"
# print("hello, world!".title())       # "Hello, World!"

# Processing multiple times
# user_name = " ROLF SMITH  "
# user_name = user_name.strip()  # "ROLF SMITH"
# user_name = user_name.title()  # "Rolf Smith"

# user_name = " ROLF SMITH  ".strip().title()
# print(user_name)

"""Exercises

    1. Using the variable below, print "Hello, world!".

greeting = "Hello, world"

You can add the missing exclamation mark using string concatenation, format, or f-strings. The choice is yours.

    2. Ask the user for their name, and then greet the user, using their name as part of the greeting.
    The name should be in title case, and shouldn't be surrounded by any excess white space.

For example, if the user enters "lewis ", your output should be something like this:

Hello, Lewis!

    3. Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".

Remember that we can only concatenate strings to other strings, so you will have to convert the integer to a
string before you can perform the concatenation.

    4. Format and print the information below using string interpolation:

title = "Joker"
director = "Todd Phillips"
release_year = 2019

The output should look like this:

Joker (2019), directed by Todd Phillips

Once you're done with the exercises, make sure to check your answers against our solutions.
If you have an alternative solution, feel free to share it on our Discord server!"""

# 1 - Using the variable below, print "Hello, world!"
# You can add the missing exclamation mark using string concatenation, format, or f-strings. The choice is yours.
greeting = "Hello, world"
print(greeting + "!")

# 2 - Ask the user for their name, and then greet the user, using their name as part of the greeting.
# The name should be in title case, and shouldn't be surrounded by any excess white space
name = input("Please enter your name: ")
print(name.strip().title())

# 0r:
name = input("Please enter your name: ").strip().title()
print(f"Hello, {name}!")

# 3 - Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29"
print("I am " + "29")

# Or:
age = 29
output_string = "I am " + str(age)
print(output_string)

# 4 - Format and print the information below using string interpolation:
title = "Joker"
director = "Todd Phillips"
release_year = 2019
# The output should look like this: " Joker (2019), directed by Todd Phillips"
print(f"{title} ({release_year}), directed by {director}")
