
# Day 13 - Scope and Returning Values from Functions

# names = ["Mike", "Fiona", "Patrick"]
# x = 53657
#
# def add(a, b):
#     print(a, b)
#
# print(globals())
#
# def add(a, b):
#     print(locals())
#     print(a, b)
#
# add(7, 25)
#
#
# def greet(name):
#     print(locals())
#     greeting = f"Hello, {name}!"
#     print(locals())
#     print(greeting)
#
# greet("Phil")
"""Exercises

1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to
raise the base to. The function should return the result of this operation. Remember we can perform exponentiation
using the ** operator."""

def exponentiate(a,b):
    return a ** b

print(exponentiate(2,16))

"""2) Define a process_string function which takes in a string and returns a new string which has been converted to 
lowercase, and has had any excess whitespace removed."""

def process_string():
    string = input("Enter a string: ")
    convert_string = string.strip().lower()
    print(convert_string)

print(process_string())

# or :
def process_string(raw_string):
    return raw_string.strip().lower()


"""3) Write a function that takes in a tuple containing info about an actor and returns this data as a dictionary. 
The data should be in the following format:

("Tom Hardy", "English", 42)  # name, nationality, age

You can choose whatever key names you like for the dictionary."""
#
# def actor_info(actor):
#     name, nationality, age = actor
#
#     return {
#         "name": name,
#         "nationality": nationality,
#         "age": age
#     }
#
# actor_info(name, nationality, age)


"""4) Write a function that takes in a single number and returns True or False depending on whether or not the number is 
prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series."""

def prime():
    number = int(input("Enter a number: "))
    for divisor in range(2,number):
        if number % divisor != 0:
            return True
    else:
        return False

print(prime())

# OR:
def is_prime(dividend):
    if dividend < 2:
        return False

    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            return False

    return True
