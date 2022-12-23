
# Project Avocados

# pandas is a data analysis library designed to make working with relational data a lot easier.

import pandas as pd

movies = {
    "title": ("Inception", "Pirates of the Caribbean: The Curse of the Black Pearl"),
    "director": ("Christopher Nolan", "Gore Verbinski"),
    "year": (2010, 2003)
}

df = pd.DataFrame(movies)


print(df)
