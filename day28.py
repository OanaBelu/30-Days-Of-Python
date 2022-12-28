
# Day 28 - Type Hinting

# The benefits of type hinting:
# 1.It makes it easier to understand our code, because our helpful variable names are now accompanied by a description
# of the sort of data we expect to be assigned to them.
# 2.Most modern editors are able to make good use of our type annotations to provide more meaningful hints when we do
# things like calling functions.
# 3. We can use tools like mypy to check that our type annotations are being honoured, helping us catch bugs caused by
# passing around incorrect types.

# Installing mypy : python -m pip install mypy

# from typing import Union
#
# name: str = "Phil"
# age: int = 29
# height_metres: Union[int, float] = 1.87

# from typing import Any
#
# name: str = "Phil"
# age: int = 29
# height_metres: Any = 1.87

# from typing import List

# names: List[str]  =  ["Rick", "Morty", "Summer", "Beth", "Jerry"]


# from typing import List, Union
#
# random_values: List[Union[str, int]] =  ["x", 13, "camel", 0]

# from typing import Tuple
#
# movie: Tuple[str, str, int] = ("Toy Story 3", "Lee Unkrich", 2010)

# In Python 3.9 we won't have to import things like Tuple, List, and Dict from the typing module.
# Instead, we'll be able to use the standard tuple, list, and dict types for annotation.

# from typing import List, Tuple
#
# movies: List[Tuple[str, str, int]] = [
#     ("Finding Nemo", "Andrew Stanton", 2005),
#     ("Inside Out", "Pete Docter", 2015),
#     ("Toy Story 3", "Lee Unkrich", 2010)
# ]

# from typing import List, Tuple
#
# Movie = Tuple[str, str, int]
#
# movies: List[Movie] = [
#     ("Finding Nemo", "Andrew Stanton", 2005),
#     ("Inside Out", "Pete Docter", 2015),
#     ("Toy Story 3", "Lee Unkrich", 2010)
# ]

from typing import List, Tuple, Union

Movie = Tuple[str, str, int]

def find_movie(search_term: str, movies: List[Movie]):
    for title, director, year in movies:
        if title == search_term:
            return (title, director, year)

def show_movies(movies: List[Movie]):
    for movie in movies:
        print_movie(movie)

def print_movie(movie: Movie):
    title, director, year = movie
    print(f"{title} ({year}), by {director}")

movies: List[Movie] = [
    ("Finding Nemo", "Andrew Stanton", 2005),
    ("Inside Out", "Pete Docter", 2015),
    ("Toy Story 3", "Lee Unkrich", 2010)
]

show_movies(movies)

search_result: Union[Movie, None] = find_movie("Finding Nemo", movies)

if search_result:
    print_movie(search_result)
else:
    print("Couldn't find movie.")




"""Exercises
There's only one exercise today, because it's a big one. Take your final solution to the day 14 project 
(easy or hard version) and implement type hinting for your code.

If you're unsure of how to do something, remember that you can always look at the typing module documentation."""

