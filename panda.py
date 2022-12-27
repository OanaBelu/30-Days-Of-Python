
# Panda


# pandas is a data analysis library designed to make working with relational data a lot easier.
# There are two basic types that we need to get familiar with in order to work with pandas :
# The first of these is the DataFrame type, which is used to store tabular data. It consists of rows and columns
# which can be populated with data.
# We can create a DataFrame in several ways, one of which is using a dictionary. In this case the dictionary keys
# become the headings for the columns, and the values associated with those keys populate the cells of that column

import pandas as pd

movies = {
    "title": ("Inception", "Pirates of the Caribbean: The Curse of the Black Pearl"),
    "director": ("Christopher Nolan", "Gore Verbinski"),
    "year": (2010, 2003)
}

df = pd.DataFrame(movies)

print(df)

# The first column contains an index, and the other columns contain the data we specified in our movies dictionary.
# If we want to see some subset of this DataFrame, we can print df.head(), passing in the number of rows we want to see.
# This is going to be very useful for this project, because the data set we're using has over 18,000 rows!
# Our DataFrame is actually composed of several other structures called Series. Each column in our DataFrame is a
# Series, which just consists of the values in a given column, along with an associated index for each value.

# Often we'll want to make modifications to a DataFrame, such as removing unnecessary columns, or renaming headers.
# First, let's talk about renaming headings. We can do this by calling the rename method on a DataFrame, passing in a
# dictionary. The keys of this dictionary represent the names we want to replace, and the values associated with those
# keys show what we want to replace the existing names with.
# Like many of the methods in pandas, the rename method can be called with another keyword argument for the inplace
# parameter. This tells pandas whether we want to create a copy of the DataFrame, or whether we want to modify an
# existing DataFrame.

import pandas as pd

movies = {
    "title": ("Inception", "Pirates of the Caribbean: The Curse of the Black Pearl"),
    "director": ("Christopher Nolan", "Gore Verbinski"),
    "year": (2010, 2003)
}

df = pd.DataFrame(movies).rename(columns={"year": "release_year"})

df = pd.DataFrame(movies)
df.rename(columns={"year": "release_year"}, inplace=True)

print(df)

# Now let's talk about throwing away columns. There are actually a lot of different ways we can do this, but I'm only
# going to discuss two here for the sake of brevity. The first option we're going to be using is drop
# drop is great for if we want to just remove one or two columns from our DataFrame
# Let's use drop to get rid of the director column from the DataFrame we've been working with.

df.drop(columns="director",  inplace=True)

df = pd.DataFrame(movies)

df.rename(columns={"year": "release_year"}, inplace=True)
df = df[["title", "release_year"]]

print(df)

# Filtering by values  : Using query is fairly straightforward, we just need to provide a string which contains some
# condition to filter our DataFrame with

latest_movies = df.query("year == 2020")
nolan_movies = df.query("director == 'Christopher Nolan'")
