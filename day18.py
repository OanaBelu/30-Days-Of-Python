
# Day 18 - Imports

# Basic imports: math module contains a lot of useful tools for performing mathematical operations

import math
import random

print(math.pi * 5**2)  # 78.53981633974483

numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(sum(numbers))  # 0.9999999999999999

# math.fsum(iterable)
# Return an accurate floating point sum of values in the iterable. Avoids loss of precision by tracking multiple
# intermediate partial sums
print(math.fsum(numbers))  # 1.0

# Importing specific things from modules

from math import pi, tau
from tkinter import ttk

print(globals())

# Aliased imports

# import numpy as np
print(globals())

from math import *
print(globals())

"""Exercises

1) Import the fractions module and create a Fraction from the float 2.25. You can find information on how to create 
fractions in the documentation."""

from fractions import Fraction

print(Fraction(2.25))

# another solution :

"""2) Import only the fsum function from the math module and use it to find the sum of the following series of floats:"""

from math import fsum

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))

"""3) Import the random module using an alias, and find a random number between 1 and 100 using the randint function. 
You can find documentation for this function here."""

import random as ra
a = ra.randint(1,100)
print(a)

# another solution :
import random as rand

print(rand.randint(1, 100))

"""4) Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. 
This time the program should generate a random number, and you should tell the user whether their guess was too high, 
or too low, until they get the right number."""
import random as ra
number = ra.randint(1,100)
guessing_number = int(input("Enter a guessing number: "))
while number != guessing_number:
    guessing_number = int(input("Enter a guessing number: "))
    if number > guessing_number:
        print("Too low")
    elif number < guessing_number:
        print("Too much")
else:
    print("You guess!")

# another solution :
# import random as rand
#
# target_number = rand.randint(1, 100)
#
# guess = int(input("Enter a number: "))
#
# while guess != target_number:
#     print("Wrong!")
#     guess = int(input("Enter a number: "))
#
# print("You guessed correctly!")







