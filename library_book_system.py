"""
Author: Omario Gooding
Date: July 10, 2026
Assignment: Library Book Management System
Tier Attempted: Base Level

Description:
This program creates a small library collection using Book objects.
It can display books, check books out, return books, sort them by title,
and show only the books that are available.

"""


class Book:
    """Represents one book in the library."""

    def __init__(self, title, author, isbn, year, genre):
        """Set up the information for a new book."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None

    def __str__(self):
        """Return the book information as one formatted string."""
        return (
            f"{self.isbn:<17} "
            f"{self.title:<28} "
            f"by {self.author:<22} "
            f"{self.year:<6} "
            f"{self.genre:<18} "
            f"{self.get_status()}"
        )

    def check_out(self, patron_name):
        """Check the book out if it is available."""
        if self.available:
            self.available = False
            self.borrower = patron_name
            return True

        return False

    def return_book(self):
        """Return the book and make it available again."""
        self.available = True
        self.borrower = None
        return f"'{self.title}' has been returned and is now available."

    def get_status(self):
        """Return the current checkout status of the book."""
        if self.available:
            return "Available"

        return f"Checked out to {self.borrower}"


# Starter library collection
collection = [
    Book(
        "The Great Gatsby",
        "F. Scott Fitzgerald",
        "978-0743273565",
        1925,
        "Classic Fiction"
    ),
    Book(
        "Educated",
        "Tara Westover",
        "978-0399590504",
        2018,
        "Memoir"
    ),
    Book(
        "Dune",
        "Frank Herbert",
        "978-0441013593",
        1965,
        "Science Fiction"
    ),
    Book(
        "Things Fall Apart",
        "Chinua Achebe",
        "978-0385474542",
        1958,
        "Historical Fiction"
    ),
    Book(
        "The Hobbit",
        "J.R.R. Tolkien",
        "978-0547928227",
        1937,
        "Fantasy"
    ),
    Book(
        "Becoming",
        "Michelle Obama",
        "978-1524763138",
        2018,
        "Memoir"
    )
]


print("=== Full Collection ===")

for book in collection:
    print(book)


print()
print("=== Checkout Tests ===")

first_result = collection[0].check_out("Jordan")

if first_result:
    print(f"'{collection[0].title}' checked out to Jordan.")
else:
    print(f"'{collection[0].title}' is already checked out.")


second_result = collection[1].check_out("Priya")

if second_result:
    print(f"'{collection[1].title}' checked out to Priya.")
else:
    print(f"'{collection[1].title}' is already checked out.")


# Try checking out the first book again
repeat_result = collection[0].check_out("Alex")

if repeat_result:
    print(f"'{collection[0].title}' checked out to Alex.")
else:
    print(f"'{collection[0].title}' is already checked out.")


print()
print("=== Return Test ===")
print(collection[1].return_book())


print()
print("=== Collection Sorted by Title ===")

sorted_collection = sorted(collection, key=lambda book: book.title)

for book in sorted_collection:
    print(book)


print()
print("=== Available Books ===")

available_books = [book for book in collection if book.available]

for book in available_books:
    print(book)