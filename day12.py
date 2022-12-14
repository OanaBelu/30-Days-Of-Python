# Day 12 - Functions

# all of our function definitions should be followed by two empty lines

def get_even_numbers():
    for number in range(1, 11):
        print(number * 2)


get_even_numbers()


# Function parameters and arguments
def x_print(requested_output, quantity):
    for _ in range(quantity):
        print(requested_output)


x_print("Hello", 5)


#  Keyword arguments are an alternative to positional arguments, where we specifically tie an argument’s value
#  to a parameter name
def x_print(requested_output, quantity):
    for _ in range(quantity):
        print(requested_output)


x_print(requested_output="Hello", quantity=5)

"""Exercises

1) Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should 
print the result of the arithmetic operation indicated by the function name.

When orders matters for an operation, the first argument should be treated as the left operand, and the second argument 
should be treated as the right operand. For example, if the user passes in 6 and 2 to subtract, the result should be 4, 
not -4.

You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you 
should print a warning instead of calculating their division."""


def add(a, b):
    return a + b


def substract(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def divide(a, b):
    if b == 0:
        print("Division by zero!")
        exit()
    if a >= b:
        return a / b
    else:
        return b / a


def multiply(a, b):
    return a * b


print(add(2, 8))
print(substract(2, 8))
print(divide(2, 8))
print(multiply(2, 8))

"""2) Define a function called print_show_info that has a single parameter. The argument passed to it will be a 
dictionary with some information about a T.V. show. For example:"""


def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} season(s)")


tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

print_show_info(tv_show)

# The print_show_info function should print the information stored in the dictionary, in a nice way. For example:

#  Breaking Bad (2008) - 5 seasons
#
# Remember you must define your function before calling it!

"""3) Below you’ll find a list containing details about multiple TV series."""


def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} season(s)")


series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]
for show in series:
    print_show_info(show)

"""Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for 
each iteration, passing in each dictionary. You should end up with each series printed in the appropriate format."""

"""4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical 
whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.

In the day 7 project, we saw a number of ways to reverse a sequence, and you can use this to verify whether a string is 
the same backwards as it is in its original order. You can also use a slicing approach. Once you’ve found whether or 
not a word is a palindrome, you should print the result to the user.

Make sure to clean up the argument provided to the function. We should be stripping whitespace from both ends of the 
string, and we should convert it all to the same case, just in case we’re dealing with a name, like “Hannah”.

You can find our solutions to the exercises here."""


def polidrom():
    word = str(input("Enter a word: ").lower().strip())
    reverse_word = reversed(word)
    if list(word) == list(reversed(word)):
        print("The word is a polidrome.")
    else:
        print("The word it is not a polidrome.")


polidrom()


# Or Instead of using lists, we could also use join to create a string from the reversed

def is_palindrome(word):
    word = word.strip().lower()
    reversed_word = reversed(word)

    if word == "".join(reversed_word):
        print(True)
    else:
        print(False)


is_palindrome("Hannah")  # True
is_palindrome("Fred")  # False


# Or Instead of using lists, let use slices, as they offer an extremely elegant solution in this case
def polidrom():
    word = str(input("Enter a word: ").lower().strip())
    if word == word[::-1]:
        print("The word is a polidrome.")
    else:
        print("The word it is not a polidrome.")


polidrom()
