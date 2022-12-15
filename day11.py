
# Day 11: - Sets

# Sets are a little different to the collections we've looked at so far, in that they're not reliably ordered
# If we create a list or a tuple and print it, we know that the items will show up in the order we defined them.
# This isn't the case for a set.
# Sets can also only contain unique elements, much like we saw with dictionary keys.
# In fact, we can really think of a set as a dictionary which only contains keys.
# They're therefore very useful for filtering values, and it's also extremely efficient to perform these
# kinds of membership tests for sets

# Defining a set : set()
vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}

# nested_sets = {{1,  2,  3},  {"a",  "b",  "c"}}  # TypeError: unhashable type: 'set'
vegetables.add("potato")
print(vegetables)  # {'lettuce', 'broccoli', 'onion', 'potato', 'carrot'}

# The union of two sets is essentially the combination of the two sets
letters = {"a", "b", "c"}
numbers = {1, 2, 3}
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}

# When we find the intersection of two sets, we get a new set containing the elements common to both sets
mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}
mod_6 = mod_2.intersection(mod_3)
print(mod_6)  # {18, 12, 6}

# We have to be a little bit careful when using difference, because unlike the other set operations we've mentioned,
# with difference the order of the sets matters
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
print(bundle_1.difference(bundle_2))  # {'Final Fantasy VII', 'Cyberpunk 2077'}
print(bundle_2.difference(bundle_1))  # {'Halo Infinite', 'Doom Eternal'}

# symmetric_difference gives us all of the items which only feature in one of the sets.
# Unlike difference the order of the sets doesn't matter.
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
print(
    bundle_1.symmetric_difference(bundle_2))  # {'Cyberpunk 2077', 'Final Fanstay VII', 'Halo Infinite', 'Doom Eternal'}

# We can only call the set operator methods on sets, but we can actually pass in any collection we like into the method
# Checking if items are in collections
print("j" in "Python")  # False
print("n" in "Python")  # True

student = {
    "name": "Eric Cartman",
    "age": 10,
    "school": "South Park Elementary"
}

print("grades" in student)  # False
print("school" in student)  # True

"""Exercises

1) Create an empty set and assign it to a variable.

2) Add three items to your empty set using either several add calls, or a single call to update.

3) Create a second set which includes at least one common element with the first set.

4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.

5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their 
number was within the range you specified."""

# 1) Create an empty set and assign it to a variable
set = set()

# for number in range(0,4):
#     set.add(number)
#     print(set)

# 2) Add three items to your empty set using either several add calls, or a single call to update
set.update(range(1, 4))
print(set)

# 3) Create a second set which includes at least one common element with the first set.
second_set = {2, 3}

# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
union = set.union(second_set)
print(f'The union of the 2 sets is : {union}')

intersection = set.intersection(second_set)
print(f'The intersection of the 2 sets is : {intersection}')

symetric_diff = set.symmetric_difference(second_set)
print(f'The symetric difference of the 2 sets is : {symetric_diff}')

# Or this way:
# set2 = set()
# set2.update(range(1, 4))
#
# random_values = {"r", 1, ("Python", "C", "Rust")}
#
# print(set2.union(random_values))
# print(set2.symmetric_difference(random_values))
# print(set2.intersection(random_values))


# 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their
# number was within the range you specified.

sequence = range(0,20)
number = int(input("Please enter a number : "))

if number in sequence :
    print("The number you choose is in the sequence!")
else:
    print("The number you choose is not in the sequence!")

# Or :
numbers = range(27, 54)
user_number = int(input("Enter a number: "))

if user_number in numbers:
    print("Your number is in the valid range.")
else:
    if user_number < numbers[0]:
        print("Your number is too low.")
    else:
        print("Your number is too high.")
