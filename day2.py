
# Day 2 - Strings, Variables, and Getting Input from Users

# Strings in Python are ordered sequences of zero or more characters
# We can use single or double quotes, but nor both in the same time
print("Hello, world!")
# We can name values in Python using an assignment operation

name = "Oana Belu"

# Variable names can include letters, numbers, and underscore (_) characters
# Variable names can’t start with a number, though starting with an underscore is allowed
# Variable names are case-sensitive, but can be in any case
# We should use descriptive names for your variables
# we have to make sure to always define our variables before we use them in the code.
# If we don’t, Python is going to raise a NameError exception

# 1 input
# print("Please enter your name:")
# input()

# 2 input is actually capable of providing its own prompt
# input("Please enter your name:")

# 3 We can also assign this string to a variable if we want
# name = input("Please enter your name: ")

"""Exercises

Now that we’ve covered how to use strings, variables, and the input function, it’s time to practice with some exercises.

    1. Ask the user for their name and age, assign theses values to two variables, and then print them.
    2. Investigate what happens when you try to assign a value to a variable that you’ve already defined. 
    Try printing the variable before and after you reuse the name.
    3. Below you’ll find some code with a number of errors. Try to go through the program line by line and fix 
    the issues in the code. I’d encourage you to try running the program while you’re working on it, as reading 
    the error messages is great practice for debugging your own programs.
    
hourly_wage = input("Please enter your hourly wage: ')

prnt("Hourly wage: ")
print(hourlywage)
print("Hours worked: ")
print(hours_worked)

hours_worked = input("How many hours did you work this week? ")

"""

# 1 - Ask the user for their name and age, assign these values to two variables, and then print them
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(name + " " + age)

# 2 - Investigate what happens when you try to assign a value to a variable that you’ve already defined.
#     Try printing the variable before and after you reuse the name.
name = input("Please enter your name: ")
print(name)
name = "Delia"


name = input("Please enter your name: ")
name = "Delia"
print(name)

# 3 - Below you’ll find some code with a number of errors. Try to go through the program line by line and fix
#     the issues in the code
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week?: ")

print("Hourly wage: ", hourly_wage)
print("Hours worked: ", hours_worked)
