
# Day 21 - Splitting Code Into Multiple Files

import json

print(globals())

import math

print(math.pi)  # 3.14

# Why split your code into files ? - In programming, readability and maintainability trump speed of writing any day
# as you write more, it'll make it much more difficult to read and modify
# When we separate code into files, it's important we have a reason for putting some code in a certain file.
# Usually, we go by concerns. Code that does one thing goes into one file, and code that does something different
# goes into a different file.

# For example, we might have one file for user interaction (prints and inputs), and another file for data storage
# (saving and retrieving things from a file)

# Separating files by concerns, assuming we give the files good names, also helps us find code more easily.
# If you have two fils called data_storage.py and user_menu.py, you know what you're going to find in each!

# Using files and folders also does wonders for organisation. You could put files related to working with different
# types of data storage into one folder, for example.

import myfile
print("What's going on?")
import myfile

try:
    myfile.get_user_age()
except ValueError:
    print("That's not a valid value for your age!")


