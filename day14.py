
# Day 14 - Working with Files

# The open function - When we call open, it's going to gives us back a means of accessing the data inside a file
# we specify.
# We can actually pass a lot of arguments to open, which change its behaviour, but we're going to start with just one:
# the name of the file we want to access.
# First, we need to create a file to access. The file we're going to be working with to start is a simple text
# file which I've added to my repl alongside the main.py file.

# we need to create a file to access
# The file is called example.txt, and its content is a short message in plain text:
example_file = open("example.txt")
print(example_file.read())
example_file.close()

# Opening files in different modes :
# By default, open is going to open our files in read mode, which is why we only have read access.
# This mode is denoted by the string, "r"

example_file = open("example.txt", "r")
print(example_file.read())
example_file.close()

example_file = open("example.txt", mode="r")
print(example_file.read())
example_file.close()

with open("example.txt", "r") as example_file:
    print(example_file.read())

# These are all functionally equivalent.
# We also have write mode, denoted by the string, "w".

write_file = open("write_example.txt", "w")
write_file.write("Welcome to the world, write_example.txt!")
write_file.close()

with open("write_example.txt", "w") as write_file:
    write_file.write("Welcome to the world, write_example.txt!")


# Append mode is another type of write mode, and is denoted by the string, "a"
write_file = open("write_example.txt", "a")
write_file.write("\nNow you have two lines! You're growing up so fast!")
write_file.close()

with open("write_example.txt", "a") as write_file:
    write_file.write("\nNow you have two lines! You're growing up so fast!")


# Context managers for working with files : with open...as
# CSV data : CSV stands for comma separated values
# Let's start by creating a new repl, and placing a file in our new repl called iris.csv, and we're going to
# put the following data inside

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.read()

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.read().split("\n")

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

irises = []

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

headers = iris_data[0].strip().split(",")
irises = []

for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers, iris))

    irises.append(iris_dict)

"""Exercises

Rewrite the following piece of code using a context manager:

 f = open("hello_world.txt", "w")
 f.write("Hello, World!")
 f.close()

Use append mode to write "How are you?" on the second line of the hello_world.txt file above.

Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format."""

f = open("hello_world.txt", "w")
f.write("Hello, World!")
f.close()

with open("hello_world.txt", "w") as f:
    f.write("Hello, World!")


f = open("hello_world.txt", "a")
f.write("\nHow are you?")
f.close()

with open("hello_world.txt", "a") as f:
    f.write("\nHow are you?")


irises = [
    {'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.9', 'sepal_width': '3',   'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.6', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '5',   'sepal_width': '3.6', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '7',   'sepal_width': '3.2', 'petal_length': '4.7', 'petal_width': '1.4', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '4.9', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '5.5', 'sepal_width': '2.3', 'petal_length': '4',   'petal_width': '1.3', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.5', 'sepal_width': '2.8', 'petal_length': '4.6', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
    {'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6',   'petal_width': '2.5', 'species': 'Iris-virginica'},
    {'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9', 'species': 'Iris-virginica'},
    {'sepal_length': '7.1', 'sepal_width': '3',   'petal_length': '5.9', 'petal_width': '2.1', 'species': 'Iris-virginica'},
    {'sepal_length': '6.3', 'sepal_width': '2.9', 'petal_length': '5.6', 'petal_width': '1.8', 'species': 'Iris-virginica'},
    {'sepal_length': '6.5', 'sepal_width': '3',   'petal_length': '5.8', 'petal_width': '2.2', 'species': 'Iris-virginica'}
]


for iris in irises:
    sepal_length, sepal_width, petal_length, petal_width, species = iris.values()
    print(f"{sepal_length},{sepal_width},{petal_length},{petal_width},{species}")

for iris in irises:
    print(",".join(iris.values()))

with open("iris_2.csv", "w") as iris_file:
    for iris in irises:
        iris_file.write(",".join(iris.values()) + "\n")




