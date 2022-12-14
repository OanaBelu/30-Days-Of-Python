"""The brief

Below you'll find a list which contains the relevant data about a selection of movies. Each item in the list is a
tuple containing a movie name and movie budget in that order:
For this project, your program should do the following:

    1. Calculate the average budget of all movies in the data set.
    2. Print out every movie that has a budget higher than the average you calculated. You should also print out how
    much higher than the average the movie's budget was.
    3. Print out how many movies spent more than the average you calculated.

If you want a little extra challenge, allow users to add more movies to the data set before running the calculations."""

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)

]

media = 0
x = 0
above_average_movies = []
for movie in movies:
    media = media + movie[1]
    x += 1

average_budget = int(media / x)
print(f'The average budget is: {average_budget}')

for movie in movies:
    if movie[1] > average_budget:
        above_average_movies.append(movie)
        extra_budget = movie[1] - average_budget
        print(f'{movie[0]} cost {movie[1]} : {extra_budget} over average budget.')
print(f'There are {len(above_average_movies)} movies with budget over average budget.')


# or :

new_movie_count = int(input("Enter how many new movies you wish to add: "))

for _ in range(new_movie_count):
    name = input("Enter new movie name: ")
    budget = int(input("Enter new movie budget: "))
    new_movie = (name, budget)
    movies.append(new_movie)

high_budget_movies = []
total_budget = 0

for movie in movies:
    total_budget = total_budget + movie[1]

average_budget = int(total_budget / len(movies))

for movie in movies:
    if movie[1] > average_budget:
        high_budget_movies.append(movie)
        over_average_cost = movie[1] - average_budget
        print(f"{movie[0]} cost ${movie[1]}: ${over_average_cost} over average.")

print(f"There were {len(high_budget_movies)} movies with over average budgets.")