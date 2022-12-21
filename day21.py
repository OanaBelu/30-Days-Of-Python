
# Day 21 - Splitting Code Into Multiple Files

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
#
# from user_interactions import myfile
#
# print("What's going on?")
#
# try:
#     myfile.get_user_age()
# except ValueError:
#     print("That's not a valid value for your age!")
#
# # What (not) to name your files json for example
#
# """Your files work in the same way as modules
#
# Everything we could do with external modules, we can do with our own files:
#
#     Importing the whole file with import myfile and then referring to things as myfile.x.
#     Importing specific things with from myfile import x.
#     Aliased imports.
#     We can do from myfile mport * (although it's discouraged).
# """
#
# # For example, create a folder in your project called user_interactions and move myfile.py into it
# from user_interactions.myfile import get_user_age
#
# try:
#     get_user_age()
# except ValueError:
#     print("That's not a valid value for your age!")
#
# # When importing, the dot (.) means something like "inside".
# # In the example above, we're therefore importing myfile from inside user_interactions
# # If you have multiple sub-folders, you will need to use multiple . to separate the different levels of folders and
# # files, like this: from folder.subfolder.module import something_in_the_module
#
# import user_interactions.myfile
#
# user_interactions.myfile.get_user_age()

# Script mode vs. module mode
# When we run a file (e.g. in repl.it, that's main.py), we say that file is ran in "script mode".#
# When we import a file, that file runs in "module mode".
import user_interactions.myfile

print(__name__)

"""Remember that when we import, we run the file. Therefore the first line of output belongs to myfile.py, and the 
second line of output belongs to main.py.

The file that we run always has a __name__ variable with a value of "__main__". That is simply how Python tells us 
that we ran that file.

Any file that doesn't have a __name__ equal to "__main__" was imported.

Try moving things around and see how the output created by myfile.py changes!"""

# Day 21 Exercise - 30 Days Of Python
# Your task is to split this code into files.
# Create a new repl and split the code how you see fit!

import json

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """
BOOKS_FILE = 'books.json'


def menu():
    create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


def create_book_table():
    try:
        with open(BOOKS_FILE, 'x') as file:
            json.dump([], file)  # initialize file as empty list
    except FileExistsError:
        pass


def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    insert_book(name, author)


def insert_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    save_all_books(books)


def get_all_books():
    with open(BOOKS_FILE, 'r') as json_file:
        return json.load(json_file)


def save_all_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file)


def list_books():
    for book in get_all_books():
        read = 'YES' if book['read'] == '1' else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    mark_book_as_read(name)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    save_all_books(books)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    delete_book(name)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    save_all_books(books)


menu()