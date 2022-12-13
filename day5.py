
# Day 5 - Conditionals and Booleans

# Booleans :
# We only ever have two Boolean values, and in Python those values are the words True and False
# Importantly, True is also not the same thing as the string "True"
# Comparison operators
# ASCII codes of the characters are used to determine which value is greater than the other
# print("A" < "a")  # True  # The ASCII code for A is 65, while a is 97

# We can use a function called id to find out where something is being stored, represented as a long series
# of numbers. This long series of numbers is an address that references a location in memory.
# We can print these memory addresses to verify that the two lists are not in fact the same

# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(id(a))  # 139806639351360
# print(id(b))  # 139806638418944
#
# print(a == b)  # True
# print(a is b)  # False

# a = [1, 2, 3]
# b = a
#
# print(id(a))  # 139685763327296
# print(id(b))  # 139685763327296
#
# print(a == b)  # True
# print(a is b)  # True

# Conditional statements:
# The most basic conditional statement uses a single keyword: if
# name = input("Please enter your name: ")
#
# if name:  # Checks the truth value of name by calling bool
#       print(f"You entered {name}")
# else:
#       print("You didn't type anything")

"""Exercises

1) Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding
the memory address for a given value, and we can compare memory addresses to check for identity.

2) Try to use the is operator or the id function to investigate the difference between this:

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

And this:

numbers = [1, 2, 3, 4]
numbers.append(5)

Are new_numbers and numbers the same thing? What about numbers before and after we append 5?

3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.

4) Write a program to determine whether an employee is owed any overtime. You should ask the user how many
hours the employee worked this week, as well as the hourly wage for this employee.

If the employee worked more than 40 hours, you should print a message which says the employee is due some
additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each
 hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime."""