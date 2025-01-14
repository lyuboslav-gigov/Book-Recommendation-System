"""
File: bookstore.py
Author: Lyuboslav Gigov
Purpose: Defines the Bookstore class that manages a collection of books.
It includes functionality to load books from a file, sort them,
and manage inventory based on book genre and attributes.
"""

import sys
from science_fiction import ScienceFiction
from romance import Romance
from biography import Biography
from encyclopedia import Encyclopedia

FILE_NAME = "Bookstore_Inventory.txt"


class Bookstore:
    """
    A bookstore class that handles loading books from a text file
    (representing the bookstore inventory) into a
    collection.

    Attributes:
        __books (list): A private list of books loaded from the inventory file.
    """

    def __init__(self):
        """Initializes the Bookstore and loads books
        from the specified inventory file."""
        self.__books = self.load_books()

    @staticmethod
    def load_books():
        """
        Processes books from a predefined text file
        into a list.

        The method reads a formatted text file where each line
        corresponds to a book with its details.
        It processes two sections of the file: the first with
        detailed characteristics (8 fields per line)
        and the second with general information (6 fields per line).

        Raises:
            FileNotFoundError: If the specified file cannot be found.
            ValueError: If any line in the file does
            not contain the expected number of fields,
            or if an invalid book genre is found.

        Returns:
            list: A list of book objects created from the file data.
        """
        books = []
        try:
            with open(FILE_NAME, "r") as readfile:
                lines = readfile.readlines()
                lines = [
                    line.strip() for line in lines
                ]  # Strip newline characters from all lines
                # Process the first part of the file (the first 7 lines)
                for line in lines[:7]:
                    line = line.strip()
                    parts = [part.strip() for part in line.split(";")]
                    if len(parts) != 8:
                        raise ValueError(
                            f"Incorrect number of fields."
                            f"Expected 8, got {len(parts)}. Line: {line}"
                        )

                    title, author, genre = parts[0], parts[1], parts[2]
                    price = float(parts[3])
                    year = int(parts[4])
                    isbn = parts[5]
                    genre_characteristic_1, genre_characteristic_2 = int(
                        parts[6]
                    ), int(parts[7])

                    if genre == "Science Fiction":
                        book = ScienceFiction(
                            title,
                            author,
                            price,
                            year,
                            isbn,
                            genre_characteristic_1,
                            genre_characteristic_2,
                        )
                    elif genre == "Romance":
                        book = Romance(
                            title,
                            author,
                            price,
                            year,
                            isbn,
                            genre_characteristic_1,
                            genre_characteristic_2,
                        )
                    else:
                        raise ValueError(
                            f"Invalid genre: {genre}, please check"
                            f"the spelling"
                            f"in the input file and try again."
                        )
                    books.append(book)

                # Process the remaining lines
                for line in lines[7:]:
                    line = line.strip()
                    parts = [part.strip() for part in line.split(";")]
                    if len(parts) != 6:
                        raise ValueError(
                            f"Incorrect number of fields."
                            f"Expected 6, got {len(parts)}. Line: {line}"
                        )

                    title, author, genre = parts[0], parts[1], parts[2]
                    price = float(parts[3])
                    year = int(parts[4])
                    isbn = parts[5]

                    if genre == "Biography":
                        book = Biography(title, author, price, year, isbn)
                    elif genre == "Encyclopedia":
                        book = Encyclopedia(title, author, price, year, isbn)
                    else:
                        raise ValueError(
                            f"Invalid genre: {genre},"
                            f"please check the spelling"
                            f"in the input file and try again."
                        )
                    books.append(book)

        except FileNotFoundError:
            print(
                "File containing bookstore inventory not found."
                "Please check that it has the right name!"
            )
            sys.exit()
        except ValueError as ve:
            print(ve)
            sys.exit()

        return books
