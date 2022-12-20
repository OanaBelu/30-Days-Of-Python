
# Day 19 - Exception Handling

# SyntaxError, NameError, and TypeError
# StopIteration - when we iterate over some iterable in a for loop
#
# while  True:
#     user_number = input("Please enter a whole number: ")
#
#     if  user_number.isnumeric():
#         number = int(user_number)
#         break
#     else:
#         print("You didn't enter a valid integer!")
#
# while  True:
#     user_number = input("Please enter a whole number: ")
#
#     if user_number.lstrip("-").isnumeric():
#         number = int(user_number)
#         break
#     else:
#         print("You didn't enter a valid integer!")
#
#
# while True:
#     try:
#         number = int(input("Please enter a whole number: "))
#         break
#     except ValueError:
#         print("You didn't enter a valid integer!")
#
#
# # I'm using fsum here, just because the numbers are likely to be floats rather than integers in many cases
# import math
#
# def average(numbers):
#     mean = math.fsum(numbers) / len(numbers)
#     print(mean)

"""Okay, so let's think about potential issues:

    The user may pass in an empty collection, so then we're going to get 0 returned from len. That's going to lead to 
    division by 0, which is not allowed. In this case, we get a ZeroDivisionError.
    The user may pass in something which isn't a collection. This is going to give us a TypeError, because fsum expects
     an iterable, and len expects a collection.
    The user may pass in a collection which contains things which aren't numbers. This is also going to be a TypeError.

That gives us two exceptions we need to take care of: ZeroDivisionError and TypeError."""
import math

def average(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    except ZeroDivisionError:
        print(0)
    except TypeError:
        print("You provided invalid values!")

# The else clause
# The finally clause : finally is very special, because it will always run.
# If we return from a function inside the try statement, finally will interrupt that return to run its own code first.
# You can see an example by running this code :
# def finally_flex():
#     try:
#         return
#     finally:
#         print("You return when I say you can return...")
#
# finally_flex()

"""Exercises

1) Create a short program that prompts the user for a list of grades separated by commas. Split the string into 
individual grades and use a list comprehension to convert each string to an integer. You should use a try statement to 
inform the user when the values they entered cannot be converted."""
grades = input("Please enter your grades, separated by commas: ").split(",")
grades = [grade.strip() for grade in grades]


try:
    grades = [int(grade) for grade in grades]
except ValueError:
    print("The grades you entered were in an invalid format.")


"""2) Investigate what happens when there is a return statement in both the try clause and finally clause of a try 
statement."""

def func():
    try:
        return "Returned from the try clause!"
    finally:
        return "Returned from the finally clause!"

print(func())  # "Returned from the finally clause!"


"""3) Imagine you have a file named data.txt with this content:

There is some data here!

Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file 
doesn't exist. Once you've verified your solution works with an actual file, delete the file and see if your try 
block is able to handle it.

When files don't exist when you try to open them, the exception raised is FileNotFoundError."""

example_file = open("example.txt", "r")
print(example_file.read())
example_file.close()


try:
    with open("example1.txt", "r") as text_file:
        print(text_file.read())

except FileNotFoundError:
    print("Error: No such file or directory: 'example1.txt'")

print(example1.read())
example1.close()

