
# Day 7 - split, join, and Slices

# Converting tuples and lists to strings: the join method
# We call join on a string, and that string is what we want to place between the items in the collection we want to
# glue together

# project_authors = ["Mike", "Sofia", "Helen"]
# project_authors = ", ".join(project_authors)
# print(f"The people who worked on this project are: {project_authors}.")

# or:
#
# project_authors = ["Mike", "Sofia", "Helen"]
# print(f"The people who worked on this project are: {', '.join(project_authors)}.")

# One thing to be aware of when using join is that we can only join collections of strings
# If we have a list of numbers, we have to convert each number to a string first.
#
# numbers = [1, 2, 3, 4, 5]
#
# stringified_numbers = []
#
# for number in numbers:
#     stringified_numbers.append(str(number))
#
# print(', '.join(stringified_numbers)) # 1, 2, 3, 4, 5

# Splitting up a string: list
# user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
# numbers_list = user_numbers.split(",")
#
# print(numbers_list) # ['1', '2', '3', '4', '5']

# Splitting up a string: tuple
# user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
# numbers_tuple = tuple(user_numbers.split(","))
#
# print(numbers_tuple) # ('1', '2', '3', '4', '5')

# sample_string = "Python"
#
# print(list(sample_string)) # ['P', 'y', 't', 'h', 'o', 'n']
# print(tuple(sample_string)) # ('P', 'y', 't', 'h', 'o', 'n')

# The newline character : \n
# print("Super Special Mega Awesome Program\n\nBy Phillip Best")

# Slicing
# original_string = "Python"
#
# print(original_string[3:])  # hon
# print(original_string[3:-1])  # ho
# print(original_string[::3])  # Ph
# print(original_string[3:-1:2]) # h
# print(original_string[:]) # Python

"""Exercises

1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names,
and then assign each name to a different variable. For this exercise, you can assume that the user has a single given
name and a single surname.

2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only
join collections of strings, so you’re going to need to do some initial processing of the list of numbers.

3) Below you’ll find a short list of quotes:

 quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
 ]

Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract
the text from each string, without these extra quote marks, and print each quote.

You may also want to try a solution using strip.

4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess
whitespace in the user’s input, so you’re going to have to process the string before you find its length.

If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them
how many how many characters are in the text overall, and you can also provide them a word count."""

# 1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names,
# and then assign each name to a different variable. For this exercise, you can assume that the user has a single given
# name and a single surname.
name_surname = input("Please enter your name and surname: ").split()
name = name_surname[0]
surname = name_surname[1]

print(name, surname)

# 2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only
# join collections of strings, so you’re going to need to do some initial processing of the list of numbers.
first_list = [1, 2, 3, 4, 5]
empty_list = []

for i in first_list:
    empty_list.append(str(i))

print(empty_list)
print(" | ".join(empty_list))

# 3) Below you’ll find a short list of quotes:
#
#  quotes = [
#     "'What a waste my life would be without all the beautiful mistakes I've made.'",
#     "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
#     "'The very essence of romance is uncertainty.'",
#     "'We are not here to do what has already been done.'"
#  ]
#
# Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing,extract
# the text from each string, without these extra quote marks, and print each quote.
#
# You may also want to try a solution using strip.
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
 ]

for quote in quotes:
    print(quote.strip("'"))

# 4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess
# whitespace in the user’s input, so you’re going to have to process the string before you find its length.
#
# If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them
# how many how many characters are in the text overall, and you can also provide them a word count."""

sample_string = input("Please enter a word: ").strip()

character_count = len(sample_string)
word_count = len(sample_string.split())
print(f"Character count: {character_count}")
print(f"Word count: {word_count}")