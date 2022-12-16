
# Day 15 - Comprehensions

# List comprehensions are used to create a new list from some other iterable

names = ["mary", "Richard", "Noah", "KATE"]
processed_names = []

for name in names:
    processed_names.append(name.title())

print(processed_names)

names = ["mary", "Richard", "Noah", "KATE"]
processed_names = [name.title() for name in names]
print(processed_names)

names = ["mary", "Richard", "Noah", "KATE"]
names = [name.title() for name in names]
print(names)


names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = []

# Style note : it can be helpful to break the comprehension up over several lines
for name, age in zip(names, ages):
    person_data = (name.title(), age)
    people.append(person_data)

print(names)

names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = [(name.title(), age) for name, age in zip(names, ages)]
print(people)

people = [
    (name.title(), age)
    for name, age in zip(names, ages)
]
print(people)

# Set comprehensions
names = ["mary", "Richard", "Noah", "KATE"]
names = {name.title() for name in names}

# Dictionary comprehensions
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {}

for student_id, name in zip(student_ids, names):
    student = {student_id: name.title()}
    students.update(student)

# We can produce the same dictionary with a dictionary comprehension like so
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {
    student_id: name.title()
    for student_id, name in zip(student_ids, names)
}

# Comprehensions and scope
# For example, with a regular loop, we can do something like this:
names = ["Mary", "Richard", "Noah", "Kate"]
names_lower = []

for name in names:
    names_lower.append(name.lower())

print(name)  # This refers to the name variable we defined in the loop

# If we use a comprehension of the other hand, we can't do this:
names = ["Mary", "Richard", "Noah", "Kate"]
names_lower = [name.lower() for name in names]

"""Exercises

1) Convert the following for loop into a comprehension:"""

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)
print(squares)

squares=[number ** 2 for number in numbers]
print(squares)

"""2) Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values 
is title case.

Remember that iterating over a dictionary only gives us the keys by default. You can use the items method to get the 
keys and the values. See day 10 for more details."""

movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

updated_movie = {}

for key, value in movie.items():
    updated_movie.update({key: value.title()})

print(updated_movie)


# The thing we want to add is key: value.title() where the for loop is for key, value in movie.items()

movie = {key: value.title() for key, value in movie.items()}
print(movie)

