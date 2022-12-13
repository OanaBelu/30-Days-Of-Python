
# Project: Fizz Buzz

"""Today's project is actually a very common interview question, which revolves around a childhood counting game called
Fizz Buzz.

In case you're not familiar with the game, it goes like this:

    One player starts by saying the number 1.
    Each player then takes it in turns to say the next number, counting one at a time.
    If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".
    If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".
    If the number is divisible by 3and5, instead of saying the number, the player should say, "Fizz Buzz".
    If you make a mistake, you're usually eliminated from the game, and the game continues until there's only a single
    player remaining.
"""

number = int(input("Please enter a number: "))
for number in range(0,number+1):
    if number % 3 == 0:
        if number % 5 == 0:
            print("Fizz Buzz")
        else :
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

