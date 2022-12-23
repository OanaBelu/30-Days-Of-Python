
# Day 25 - Writing Idiomatic Python

# An idiom is a language, dialect, or style of speaking peculiar to a people
# Python code is said to be Pythonic when it's written in a way that adopts the idioms of the Python language,
# and which conforms to a certain set of stylistic principles

my_list = [36]

if len(my_list) == 0:
    print("The list is empty")
else:
    values = ', '.join(str(value) for value in my_list)
    print(f"The list contains: {values}")

my_list = [2,"k"]

if my_list:
    values = ', '.join(str(value) for value in my_list)
    print(f"The list contains: {values}")
else:
    print("The list is empty")


name = input("Please enter your name: ").strip().title()

if not name:
    name = "John Doe"

name = input("Please enter your name: ").strip().title() or "John Doe"
print(name)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return

a = 6
b = 0

result = divide(a, b)

if result and result.is_integer():
    print(f"{a} / {b} produces an integer result.")

numbers = [1, 54, 2, -4, -65, 23, 97, 45, 14, 19, 73, -6, 31, 92, 3]

positive_numbers = sorted(number for number in numbers if number > 0)
positive_numbers = positive_numbers[:10]

print(positive_numbers)  # [1, 2, 3, 14, 19, 23, 31, 45, 54, 73]

numbers = [1, 54, 2, -4, -65, 23, 97, 45, 14, 19, 73, -6, 31, 92, 3]

positive_numbers = sorted(number for number in numbers if number > 0)

del positive_numbers[10:]

print(positive_numbers)  # [1, 2, 3, 14, 19, 23, 31, 45, 54, 73]

proceed = input("Would you like to continue? ").strip().lower()

if proceed == "y" or proceed == "yes" :
    print("yes")


"""Exercises

1) Write a function that prompts the user for their name and then greets them. You should process the string by 
removing any whitespace and converting the string to title case.

If after processing the string you're left with an empty string, the function should replace the empty string with 
"World" in the output."""
def greets():
    name = input("Enter your name: ").strip().title()
    print(f"Hello, {name or 'World'}!")

print(greets())

"""2) Write a function to determine whether or not a string contains exclusively ASCII letters (a to z in either upper 
or lowercase).

Hint: You should look at the constants in the string module. Documentation can be found here."""

from string import ascii_letters

def is_ascii_letters(test_string):
    for character in test_string:
        if character not in ascii_letters:
            return False
    else:
        True

print(is_ascii_letters("ABNNN"))


from string import ascii_letters

def is_ascii_letters(test_string):
    return all(character in ascii_letters for character in test_string)
print(is_ascii_letters("jdhhd weueu"))

"""3) Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100 
(inclusive). Sort each of these lists into descending order (largest first), and then truncate each list so that only 
5 items remain in each."""

import random

list = [random.sample(range(1, 101), 15) for _ in range(3)]

for number in list:
    list.sort(reverse = True)
    print(list)
    del number[5:]
print(list)




