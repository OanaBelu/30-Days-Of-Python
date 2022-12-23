
# Day 24 - Advanced Exception Handling and Raising Exceptions

# The exception hierarchy:
"""BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""

# One thing you will quickly notice is that some exceptions are listed as a subcategory of another type of exception.
# For example, let's take a look at SyntaxError:
"""+-- SyntaxError
|    +-- IndentationError
|         +-- TabError
"""

numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError:
    print("Could not retrieve that value.")

numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not retrieve that value.")

# When an exception is found in a try clause, Python is going to look through the except clauses in order to see if any
# match. As soon as a matching exception is found, it's going to stop looking. This is very much like how conditional
# statements function.

# In the example above, we're now going to trigger the first except clause, because we have an IndexError, but other
# types of LookupError will trigger the second except clause, such as a KeyError.

person = {
    "name": "Phil",
    "city": "Budapest"
}

try:
    print(person["age"])  # <- Referencing an undefined key
except KeyError:
    print("The requested ")
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not")

numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError as ex:
    print(f"Error: {ex}")

# Raising an exception: raise ValueError
# raise ValueError("I raised this ValueError for no reason!")

# One thing you may not have realised is that we can put try statements inside other try statements

# def intify(number):
#     try:
#         return int(number)
#     except ValueError:
#         try:
#             f_number = float(number)
#         except ValueError:
#             raise ValueError(f"could not convert string to an integer: {number}") from None
#         else:
#             return round(f_number)
#
# with open("numbers.txt", "r") as numbers_file:
#     numbers = [int(number) for number in numbers_file]

"""Exercises

1) Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range, 
raise a ValueError and inform them that their choice was invalid."""
number = int(input("Please enter a number between 1 and 10 (inclusive): "))

if number not in range(1,11):
    raise ValueError ("Please enter a correct number!")



"""2) Below you'll find a divide function. Write exception handling so that we catch ZeroDivisionError exceptions, 
TypeError exceptions, and other kinds of ArithmeticError."""

def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Division by zero can not be done!")
    except TypeError:
        print("Both values must be numbers. Cannot divide {a} and {b}")
    except ArithmeticError:
        print("Could not complete the division. The numbers were likely too large")
    # except NameError:
    #     print("Both values must be numbers")

divide(3,3)
divide(3,0)
# divide(0,c)

"""3) Below you'll find an itemgetter function that takes in a collection, and either a key or index. Catch any instances 
of KeyError or IndexError, and write the exception to a file called log.txt, along with the arguments that caused this
 issue. Once you have written to the log file, reraise the original exception."""

def itemgetter(collection, identifier):
    return collection[identifier]

def log_exception(exception, fn, **kwargs):
    values = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())

    with open("log.txt", "a") as log_file:
        log_file.write(f"Exception: {exception}, Function: {fn}, Values: {values}\n")

def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except (IndexError, KeyError, TypeError) as ex:
        log_exception(ex, "itemgetter", collection=collection, identifier=identifier)
        raise

