
# Day 23 - Generators and Generator Expressions

# The iter function -Python has a built in function called iter which returns an iterator for the iterable we
# provide as an argument.
numbers = [1, 2, 3, 4, 5]

# If we pass this list of numbers to iter we'll get back an iterator for that list
numbers_iter = iter(numbers)

print(numbers_iter)  # <list_iterator object at 0x000001DD18D49840>
print(next(numbers_iter))  # 1
print(next(numbers_iter))  # 2
print(numbers_iter is iter(numbers_iter))  # True

# First, we need a while loop, because we want to loop a potentially infinite number of times.
# Second, we need a try statement so that we can look out for a StopIteration exception.
numbers = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers)

while True:
    try:
        number = next(numbers_iter)
    except StopIteration:
        break
    else:
        print(number)

# Generators:
# The generator syntax is actually going to be very familiar to us, because a generator is actually just a function.
# The only thing which differentiates a generator from a regular function is a special keyword called yield
# Before we dive into this new yield keyword, let's look at a simple generator example :
def first_hundred():
    for number in range(1, 101):
        yield number

g = first_hundred()
print(g)

# If you run this code, we certainly don't get anything like the numbers 1 to 100 printed to the console.
# We get this generator object: <generator object first_hundred at 0x000001A7312AFED0>

# This is actually called a generator iterator, which is what gets returned when we call any function that contains
# the yield keyword.
#
# As the name would imply, this is an iterator, and we can use it just like any other.
def first_hundred():
    for number in range(1, 101):
        yield number

g = first_hundred()

print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3

print(next(first_hundred()))  # 1
print(next(first_hundred()))  # 1
print(next(first_hundred()))  # 1

# What yield actually does is create a pause in the execution of the function body. When we call next and pass in our
# generator iterator, the code in the function body is going to run until we hit that yield keyword.
# The value after the yield keyword is what we actually want to provide before we pause the execution of the function
# body. In this way we can think of yield as something like a non-terminating return statement.

# We can see all this by adding a few print calls to first_hundred
def first_hundred():
    print("First value requested\n")

    for number in range(1, 101):
        print("Starting new iteration")
        yield number
        print("Ending this iteration\n")

g = first_hundred()

print(next(g))
print(next(g))

# First we get the "First value requested\n" string, and then we enter the for loop. At this point we get a value from
# the range object, which is assumed to number, and we print the "Starting new iteration" string

# We then encounter the yield keyword which pauses the execution of the function body, and our generator iterator spits
#out 1, which is the current value of number. This value is returned by the call to next and we print it to the console.

for number in range(1,5):
    print(number)

# yield is actually a very complicated keyword, and it can do a great deal more than what we're using it for

# In addition to creating generator iterators through functions, we can also use generator expressions
# We can use them very much like comprehensions, but they come with all the benefits of iterators that map and filter
# provide. If you've wanted to have those benefits, but didn't like the syntax for map and filter, generator
# expressions are for you
# If we want to get values out, we can either pass it to a for loop, we can destructure it, or we can use next to
# perform manual iteration
squares = (number ** 2 for number in range(1, 11))

for square in squares:
    print(square)

squares = (number ** 2 for number in range(1, 11))

print(*squares, sep=", ")

squares = (number ** 2 for number in range(1, 11))

print(next(squares))  # 1
print(next(squares))  # 4
print(next(squares))  # 9

# Remember that the values in squares get consumed when we iterate over the iterator, so you need to redefine squares
# if you want to iterate over it more than once

total = sum(number ** 2  for number in  range(1,  11))
print(total)  # 385


"""Exercises

1) Write a generator that generates prime numbers in a specified range. You can make use of your solution to 
exercise 3 from day 8 as a starting point."""
primes = []

for dividend in range(2, 34):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(str(dividend))

print(", ".join(primes))

# The first thing we need to to create a function and place all of our code inside of it
# Now we just need to turn our function into a generator by using the yield keyword. We're going to put this in the
# else branch of the inner for loop, instead of printing the dividend
def primes(limit):
    for dividend in range(2, limit+1):
        for divisor in range(2, dividend):
            if dividend % divisor == 0:
                break
        else:
            yield dividend
prime =primes(101)
print(next(prime))
print(next(prime))

"""2) Below we have an example where map is being used to process names in a list. Rewrite this code using a generator 
expression."""
# The generator expression syntax is just like the comprehensions we've been writing before.
# The only difference is that we use regular round parentheses rather than square brackets or curly braces
names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = map(lambda name: name.strip().title(), names)

names = (name.strip().split() for name in names)


"""3) Write a small program to deal cards for a game of Texas Hold'em. The order of the deal is as follows:

    The deck is shuffled.
    One card is handed to each player in order.
    A second card is handed to each player order.

Then comes the more complicated part of the deal.

    First, the top card of the deck is discarded. This is called the burn.
    Three cards are then placed in the centre of the table, which is called the flop.
    Another card is burned, meaning we discard another card from the top of the deck.
    We add another card to the centre, which is called the turn.
    We burn another card.
    Finally, there's the river, where a fifth and final card is added to the centre.

The desired output for the program is something like this:

How many players are there? 2

Player 1 was dealt: (4, hearts), (4, clubs)
Player 2 was dealt: (9, clubs), (jack, diamonds)

The flop: (jack, clubs), (4, diamonds), (king, spades)
The turn: (8, hearts)
The river: (ace, hearts)

As the example would indicate, the program should accept a variable number of players. There must be at least 
2 players, and no more than 10.

After the flop, the turn, and the river there's usually a round of betting, so if you want to extend this exercise, 
you may want to give the user the option to pause at each of these points.

Hint: We can shuffle cards using the random.shuffle method. This shuffles a sequence in-place, which means it modifies 
the original sequence. We can then create an iterator from that sequence using iter to make is easy for us to retrieve 
cards one at a time.

You can find documentation for random.shufflehere."""