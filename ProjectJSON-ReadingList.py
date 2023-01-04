
# Project JSON Reading List

# JSON stands for JavaScript Object Notation
# The json module is used for serialising and deserialising JSON data.
# all strings, which includes key names, must use double quotes ("). Single quotes (') are not valid in JSON
# the keyword true :This is entirely lowercase in JSON, unlike in Python where we use True

"""The brief
For this project the application needs to have the following functionality:

Users should be able to add a book to their reading list by providing a book title, an author's name,
and a year of publication.
The program should store information about all of these books in a Python list.
Users should be able to display all the books in their reading list, and these books should be printed
out in a user-friendly format.
Users should be able to select these options from a text menu, and they should be able to perform
multiple operations without restarting the program. You can see an example of a working menu in
the post on while loops (day 8).
This project is a bit larger than the ones we've tackled before, so make sure you tackle it one
piece at a time.

Something to note with this project is that because the books in the reading list are stored in a
Python list, when the program ends, the reading list data will be lost.

In a couple of days, in Day 14, we will come back to this project and expand it, making sure we
don't lose data when the program ends!"""


import json

def add_book():
    books = get_all_books()

    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "read": "Not read"
    })

    with open("books.json", "w") as reading_list:
        json.dump(books, reading_list)

def create_book_file():
    try:
        with open("books.json", "x") as reading_list:
            json.dump([], reading_list)
    except FileExistsError:
        pass

def delete_book(books, book_to_delete):
    books.remove(book_to_delete)

def find_books():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Please enter a book title: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books

# Helper function for retrieving data from the csv file
def get_all_books():
    with open("books.json", "r") as reading_list:
        return json.load(reading_list)

def mark_book_as_read(books, book_to_update):
    index = books.index(book_to_update)
    books[index]['read'] = "Read"

def update_reading_list(operation):
    books = get_all_books()
    matching_books = find_books()

    if matching_books:
        operation(books, matching_books[0])

        with open("books.json", "w") as reading_list:
            json.dump(books, reading_list)
    else:
        print("Sorry, we didn't find any books matching that title.")

def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print("{title}, by {author} ({year}) - {read}".format(**book))

    print()

create_book_file()

reading_list = []
menu_promp = """Please enter one of the following options:
 - 'a' to add a book
 - 'd' to delete a book
 - 'l' to list the books
 - 'r' to mark a book as read
 - 's' to search for a book
 - 'q' to quit 

 What would you like to do? """

selected_option = input(menu_promp).strip().lower()

# Get a selection from the user
selected_option = input(menu_prompt).strip().lower()

# Run the loop until the user selected 'q'
while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "d":
        update_reading_list(delete_book)
    elif selected_option == "l":
        # Retrieves the whole reading list for printing
        reading_list = get_all_books()

        # Check that reading_list contains at least one book
        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
    elif selected_option == "r":
        update_reading_list(mark_book_as_read)
    elif selected_option == "s":
        matching_books = find_books()

        # Checks that the seach returned at least one book
        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry, we didn't find any books for that search term")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    # Allow the user to change their selection at the end of each iteration
    selected_option = input(menu_prompt).strip().lower()