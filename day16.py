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
# using the get method for dictionaries, which is going to allow us to have a user select a function to run
