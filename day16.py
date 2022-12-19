# Day 16 - First Class Functions and Lambda Expressions

# first class functions :
# A programming language is said to have first class functions when functions in that language
# are treated like any other type. They're said to be "first class citizens" of the language
# his means we can pass functions in as arguments to other functions, return them from functions,
# and assign them to variables
# In Python, functions are indeed first class citizens, and we can do everything I listed above

# Assigning functions to variables:
# When we define a function using def, we provide a name for our function. Two things happen when we do this
# The function gets named according to our specification
# The function name becomes part of this representation of the function
# These are actually two very different things, and we can demonstrate this by assigning a function to a different
# variable name, and printing the values associated with these different names

def add(a, b):
    print(a + b)


adder = add

print(add)  # <function add at 0x00000277605105E0>
print(adder)  # <function add at 0x00000277605105E0>


def add(a, b):
    print(a + b)


adder = add
del add

adder(5, 4)  # 9
print(adder)  # <function add at 0x000001C34F03DBC0>

# Functions as arguments :
# Because parameters are really just variables, and arguments are the values we assign to those variables

numbers = [56, 3, 45, 29, 102, 30, 73]
highest_number = max(numbers)

print(highest_number)  # 102

# let's say I have a list of dictionaries like this:
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]


# Realistically we could order this alphabetically, or by grade average. However, in this case, max is actually trying
# to compare a whole dictionary to another dictionary using the > operator, and that's not even a legal operation
# What max expects from this function is a sortable value that is can use to determine the order of a given item

# This function accepts a dictionary, and it returns the value associated with the "grade_average" key of that
# dictionary. In our case this is an integer, and integers can be legally compared using >
def get_grade_average(student):
    return student["grade_average"]


# We can now do something like this:
def get_grade_average(student):
    return student["grade_average"]


students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=get_grade_average)
print(valedictorian)


# Returning functions from other functions:
# Using the get method for dictionaries, which is going to allow us to have a user select a function to run
# Methods are really just special types of functions

def add(a, b):
    print(a + b)


def substract(a, b):
    print(a - b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    if b == 0:
        print("You can't devide by 0!")
    else:
        print(a / b)


operations = {
    "a": add,
    "s": substract,
    "m": multiply,
    "d": divide
}

select_option = input("""Please select one of the following operations: \n  
    "a" : add,
    "s" : substract,
    "m" : multiply,
    "d" : divide"
    
What would you like to do?""")

operation = operations.get(select_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    operation(a, b)
else:
    print("Invalid selection")

# Lambda expressions: an alternative syntax for defining simple functions
# They are expressions, and the value they evaluate to is the function we want to create
# In contrast, the function definitions using the def keyword are statements
# The first part of any lambda expression is the lambda keyword
# Directly after the lambda keyword, we optionally specify any parameters for the function we want to create
# The colon marks the end of the parameters we want to define, and everything which comes afterwards is what we want
# to return from the function. In this case, what we want to return is a + b
lambda a, b: a + b
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=lambda student: student["grade_average"])
print(valedictorian)


# The lambda expression replaces the reference to a function, because the lambda expression itself yields a function
# The only function we can't replace here is divide, because divide has a conditional statement inside
def divide(a, b):
    if b == 0:
        print("You can't devide by 0!")
    else:
        print(a / b)


operations = {
    "a": lambda a, b: a + b,
    "s": lambda a, b: a - b,
    "m": lambda a, b: a * b,
    "d": divide
}

select_option = input("""Please select one of the following operations: \n  
    "a" : add,
    "s" : substract,
    "m" : multiply,
    "d" : divide"

What would you like to do?""")

operation = operations.get(select_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    print(operation(a, b))
else:
    print("Invalid selection")

# Lambda expressions are limited to single expressions and cannot contain statements
# All functions in Python are first class functions, so we can assign the functions we create with lambda expressions
# to variables if we want

add = lambda a, b: a + b

print(add(7, 8))  # 15

# If you need a function that performs any really complex logic, it's better to define a function using def, and to
# break the operations up into simpler steps so that you can use descriptive variables and comments to document
# what's happening

"""Exercises

1) Use the sort method to put the following list in alphabetical order with regards to the students' names:
You're going to need to pass in a function as a key here, and it's up to you whether you use a lambda expression, 
or whether you define a function with def."""

students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]


def sort_name(student):
    return student["name"]


students.sort(key=sort_name)
print(students)

students.sort(key=lambda student: student["name"])
print(students)

"""2) Convert the following function to a lambda expression and assign it to a variable called exp. """


def exponentiate(base, exponent):
    return base ** exponent

exp = lambda base,exponent : base ** exponent


"""3) Print the function you created using a lambda expression in previous exercise. What is the name of the function 
that was created?"""
print(exp) # <function <lambda> at 0x000001E69FDEAA20>