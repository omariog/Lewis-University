"""
Author: Omario Gooding
Date: July 10, 2026
Program: Movie Collection Manager
Tier Attempted: Base Level

Description:
This program stores a small collection of movies using a list of
dictionaries. It allows the user to add two movies, sort the collection
by year, display the top three rated movies, and calculate the average rating.

"""


def create_movie(title, year, genres, rating):
    """Create and return a dictionary for one movie."""
    movie = {
        "title": title,
        "year": year,
        "genres": genres,
        "rating": rating
    }

    return movie


def display_movies(movies, heading):
    """Display the movies in a simple formatted table."""
    print()
    print(heading)
    print("-" * 75)

    if len(movies) == 0:
        print("No movies in this collection.")
        return

    print(f'{"Title":<30} {"Year":<6} {"Genres":<25} {"Rating":>6}')
    print("-" * 75)

    for movie in movies:
        title = movie["title"]
        year = movie["year"]
        genres = " / ".join(movie["genres"])
        rating = movie["rating"]

        print(f"{title:<30} {year:<6} {genres:<25} {rating:>6.1f}")


def find_top_rated(movies, n):
    """Return a new list containing the top-rated movies."""
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    top_movies = sorted_movies[:n]
    return top_movies


def get_average_rating(movies):
    """Calculate and return the average rating of the collection."""
    if len(movies) == 0:
        return 0.0

    total_rating = 0.0

    for movie in movies:
        total_rating = total_rating + movie["rating"]

    average = total_rating / len(movies)
    return round(average, 2)


# Five starter movies stored as a list of dictionaries.
movies = [
    {
        "title": "Inception",
        "year": 2010,
        "genres": ["Sci-Fi", "Thriller"],
        "rating": 8.7
    },
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Drama"],
        "rating": 9.3
    },
    {
        "title": "The Godfather",
        "year": 1972,
        "genres": ["Crime", "Drama"],
        "rating": 9.2
    },
    {
        "title": "Black Panther",
        "year": 2018,
        "genres": ["Action", "Adventure"],
        "rating": 7.3
    },
    {
        "title": "The Lion King",
        "year": 1994,
        "genres": ["Animation", "Adventure"],
        "rating": 8.5
    }
]

# Update one value in an existing movie dictionary.
movies[0]["rating"] = 8.8

display_movies(movies, "Your Movie Collection")

# Ask the user to add exactly two new movies.
for movie_number in range(1, 3):
    print()
    print(f"Enter information for movie {movie_number}")

    title = input("Title: ")
    year = int(input("Release year: "))

    genre_text = input("Genres separated by commas: ")

    # List comprehension removes spaces around each genre.
    genres = [genre.strip() for genre in genre_text.split(",")]

    rating = float(input("Rating: "))

    new_movie = create_movie(title, year, genres, rating)
    movies.append(new_movie)

# Sort the original collection by year, from oldest to newest.
movies.sort(key=lambda movie: movie["year"])

display_movies(movies, "All Movies Sorted by Year")

top_three = find_top_rated(movies, 3)
display_movies(top_three, "Top 3 Rated Movies")

average_rating = get_average_rating(movies)

print()
print(f"Collection average rating: {average_rating:.2f}")