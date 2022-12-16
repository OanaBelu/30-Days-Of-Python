
# Project Reading List

"""The brief

For this project the application needs to have the following functionality:

    Users should be able to add a book to their reading list by providing a book title, an author's name, and a year
    of publication.
    The program should store information about all of these books in a Python list.
    Users should be able to display all the books in their reading list, and these books should be printed out in a
    user-friendly format.
    Users should be able to select these options from a text menu, and they should be able to perform multiple
    operations without restarting the program. You can see an example of a working menu in the post on while
    loops (day 8).
"""

readind_list = []
menu = """Please choose one of the option:
    - "a" if you want to add a new book
    - "l" if you want to list all the books
    - "q" if you want to exit
What would you like to do ? """

selected_option = input(menu).strip().lower()

def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year: ").strip()

    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    readind_list.append(new_book)

def list_books():
    for book in readind_list:
        print(f"{book['title']}, by {book['author']} ({book['year']})")

    print()

while selected_option != "q":
    if selected_option == "a":
        add_book()
        # print("Adding")
    elif selected_option == "l":
        if readind_list:
            list_books()
        else:
            print("You should add some books first, because your book list is empty.")
        # print("List")
    else:
        print(f"This {selected_option} is not a valid option . ")
    selected_option = input(menu).strip().lower()

