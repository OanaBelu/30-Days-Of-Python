# from typing import Union
#
# name: str = "Phil"
# age: int = 29
# height_metres: Union[int, float] = 1.87

from typing import Any

name: str = "Phil"
age: int = 29
height_metres: Any = 1.87

from typing import List, Tuple

Movie = Tuple[str, str, int]

movies: List[Movie] = [
    ("Finding Nemo", "Andrew Stanton", 2005),
    ("Inside Out", "Pete Docter", 2015),
    ("Toy Story 3", "Lee Unkrich", 2010)
]

