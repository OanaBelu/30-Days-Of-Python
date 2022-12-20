
# Day 20 - map, filter, and Conditional Comprehensions

# what comprehensions are for:
# We use a comprehension when we want to make a new collection from some other iterable.
# However, there are cases where we want to make a new collection and a comprehension isn't necessary.
# We only use a comprehension when we want to change something about the values when we make this new collection.
# For example, we might want to turn every string in a list to title case
names = ["tom", "richard", "harold"]
names = [name.title() for name in names]
print(names)
# If we just want to turn the names list to, say, a set, we can do this instead
names = set(names)
print(names)
# We don't have to bother with a much more verbose set comprehension
names = {name for name in names}
print(names)
# With this in mind, we can really think of comprehensions as a way of performing an action for every item in some
# iterable, and then storing the results

# The map function : map is a function that allows us to call some other function on every item in an iterable
# map is a way of performing some action for every item in an iterable, just like a comprehension
# Let's say I want to cube every number in a list of numbers. We can use map like so:
def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

cubed_numbers()





