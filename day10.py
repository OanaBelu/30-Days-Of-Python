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
