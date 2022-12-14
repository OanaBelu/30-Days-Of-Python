
# Day 8 - While Loops

# A while loop in many ways is quite a bit simpler than a for loop. We just need to use the while keyword, followed
# by some condition to test. If the condition evaluates to a truthy value, the loop will run one iteration, and then
# it will test the condition again.
# break allows us to exit a loop
# continue allows us to skip the remainder of the loop body for the current iteration.

# Get a number to test from the user
# dividend = int(input("Please enter a number: "))
#
# # Grab numbers one at a time from the range sequence
# for divisor in range(2, dividend):
#     # If user's number is divisible by the curent divisor, break the loop
#     if dividend % divisor == 0:
#         print(f"{dividend} is not prime!")
#         break
# else:
#     # This line only runs if no divisors produced integer results
#     print(f"{dividend} is prime!")
#
# # We can do something similar with a while loop as well:
#
# # Get a number to test from the user, and set the initial divisor to 2
# dividend = int(input("Please enter a number: "))
# divisor = 2
#
# # Keep looping until the divisor equals the number we're testing
# while divisor < dividend:
#     # If user's number is divisible by the curent divisor, break the loop
#     if dividend % divisor == 0:
#         print(f"{dividend} is not prime!")
#         break
#
#     # Increment the divisor for the next iteration
#     divisor = divisor + 1
# else:
#     # This line only runs if no divisors produced integer results
#     print(f"{dividend} is prime!")

"""Exercises

1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 
1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should 
keeping running until the user guesses the number correctly."""

# number = input("Enter a number: ")
# guessing_number = input("Enter a guessing number: ")
# while guessing_number != number:
#     print("Try again!")
#     guessing_number = input("Enter a guessing number: ")
# else:
#     print("You are correct!")
#
# # other approach:
# target_number = 47
#
# guess = int(input("Enter a number: "))
#
# while guess != target_number:
#     print("Wrong!")
#     guess = int(input("Enter a number: "))
#
# print("You guessed correctly!")
#
# # other approach:
# target_number = 47
#
# while True:
#     guess = int(input("Enter a number: "))
#
#     if guess == target_number:
#          print("You guessed correctly!")
#          break
#     else:
#         print("Wrong!")
#
# # other approach:
# target_number = 47
#
# guess = int(input("Enter a number: "))
#
# while guess != target_number:
#     if guess > target_number:
#         print("Too high!")
#     else:
#         print("Too low!")
#
#     guess = int(input("Enter a number: "))
#
# print("You guessed correctly!")

"""2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one 
character at a time."""

# string = "Python"
# for word in string:
#     if word != "o":
#         print(word)
#     else:
#         continue
#
# # other approach:
# for character in string:
#     if character == "o":
#         continue
#
#     print(character)


"""3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every 
prime number between 1 and 100."""

prime = []
for number in range(2,101):
    for divisor in range (2,number):
        if number % divisor == 0:
            break
    else:
        prime.append(str(number))
print(prime)
print(", ".join(prime))

# other approach:
# for dividend in range(2, 101):
#     for divisor in range(2, dividend):
#         if dividend % divisor == 0:
#             print(f"{dividend} is not prime!")
#             break
#     else:
#         print(f"{dividend} is prime!")
primes = []

for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(str(dividend))

print(", ".join(primes))
