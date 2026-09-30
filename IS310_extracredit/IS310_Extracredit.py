favoritemovies = [
    {"name": "Avengers: End Game", "year": 2018},
    {"name": "Top Gun Maverick", "year": 2022},
    {"name": "F1", "year": 2025},
]

def check_movie(movie):
    if movie["year"] < 2000:
        print(f"{movie['name']} was released before 2000")
    else:
        print(f"{movie['name']} was released after 2000")
        return movie["name"]

recent_movies = []

for movie in favoritemovies:
    result = check_movie(movie)
    if result is not None:
        recent_movies.append(result)

print(recent_movies)