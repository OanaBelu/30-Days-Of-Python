# Day 10 - Dictionaries

# Dictionaries - associative array, and it works a little differently to the things like lists, strings, and tuples
# In a single dictionary, each key must be unique, but different dictionaries can have the same keys as each other.
# We create a dictionary using a pair of curly braces
# We have to work in pairs of keys and values
# student1 = {
#     "name": "John Smith",
#     "grades": [88, 76, 92, 85, 69]
# }
#
# students = {"name": "John Smith", "grades": [88, 76, 92, 85, 69]}
#
# student = (
#     "John Smith",
#     [88, 76, 92, 85, 69]
# )
#
# # Append 77 to the list at index 1
# student[1].append(77)
#
# print(student)  # ('John Smith', [88, 76, 92, 85, 69, 77])
# print(student1["grades"])  # [88, 76, 92, 85, 69]
# student1["age"] = 17
#
# print(student1)


# Built-in Dictionary Methods:
# d.clear() - Clears a dictionary
# d.get(<key>[, <default>]) -Returns the value for a key if it exists in the dictionary
# The Python dictionary .get() method provides a convenient way of getting the value of a key from a dictionary
# without checking ahead of time whether the key exists, and without raising an error.
# d.get(<key>) searches dictionary d for <key> and returns the associated value if it is found. If <key> is not found,
# it returns None:
d = {'a': 10, 'b': 20, 'c': 30}
print(d.get('b')) # 20
print(d.get('z')) # None
# If <key> is not found and the optional <default> argument is specified, that value is returned instead of None:
print(d.get('z', -1)) # -1

# d.items() - Returns a list of key-value pairs in a dictionary
print(list(d.items())) # [('a', 10), ('b', 20), ('c', 30)]
print(list(d.items())[1][0]) # 'b'
print(list(d.items())[1][1]) # 20

# d.keys() -Returns a list of keys in a dictionary
print(list(d.keys())) # ['a', 'b', 'c']

# d.values() - Returns a list of values in a dictionary
print(list(d.values())) # [10, 20, 30]

# d.pop(<key>[, <default>]) - Removes a key from a dictionary, if it is present, and returns its value
d.pop('b') # 20
# d.pop(<key>) raises a KeyError exception if <key> is not in d
# d.pop('z') # KeyError: 'z'
# If <key> is not in d, and the optional <default> argument is specified, then that value is returned, and no
# exception is raised:
d.pop('z', -1) # -1

# d.popitem() -Removes a key-value pair from a dictionary and returns it as a tuple
d.popitem()  # ('c', 30)
# If d is empty, d.popitem() raises a KeyError exception: # KeyError: 'popitem(): dictionary is empty'

# d.update(<obj>) - Merges a dictionary with another dictionary or with an iterable of key-value pairs
# If <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into d. For each key in <obj>:

#     If the key is not present in d, the key-value pair from <obj> is added to d.
#     If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1) # {'a': 10, 'b': 200, 'c': 30, 'd': 400}
# In this example, key 'b' already exists in d1, so its value is updated to 200, the value for that key from d2.
# However, there is no key 'd' in d1, so that key-value pair is added from d2.
# <obj> may also be a sequence of key-value pairs, similar to when the dict() function is used to define a dictionary.
# For example, <obj> can be specified as a list of tuples
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update([('b', 200), ('d', 400)])
print(d1)  # {'a': 10, 'b': 200, 'c': 30, 'd': 400}

# Or the values to merge can be specified as a list of keyword arguments
d1.update(b=200, d=400)
print(d1)  # {'a': 10, 'b': 200, 'c': 30, 'd': 400}

d = {'foo': 100, 'bar': 200, 'baz': 300}
d['bar':'baz']
print(d)





"""Exercises

1) Below is a tuple describing an album:
Inside the tuple we have the album name, the artist (in this case, the band), the year of release, and then another
tuple containing the track list.

Convert this outer tuple to a dictionary with four keys."""

album = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
)

album_dict = {"album": album[0],
              "artist": album[1],
              "year": album[2],
              "songs": tuple(album[3])}
print(album_dict)

"""2) Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should 
print the name of the key, and then the value alongside it."""
for key in album_dict:
    print(f'{key}: {album_dict[key]}')
for key, value in album_dict.items():
    print(f"{key}: {value}")

"""3) Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key 
to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.

If you use a different album for the exercises, update the date accordingly."""

del album_dict["year"]
del album_dict["songs"]
album_dict ["release"]= "March 1st, 1973"
print(album_dict)

"""4) Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. Once you've 
tried this, repeat the step using the get method to prevent the exception being raised."""
# print(album_dict["year"])
print(album_dict.get("year", "Unknown"))
