"""
File: book.py
Author: Lyuboslav Gigov
Purpose: This module defines the Book class and its subclasses
Fiction and NonFiction.
It includes properties for managing book attributes
like title, author, price, year, and ISBN,
and methods for setting and getting these properties.
Additional functionality includes grade calculation based on
book criteria and comparison methods for sorting.
"""

import sys
from fuzzywuzzy import fuzz
import re


def match_keywords(file_name, user_keywords):
    """
    Matches user-specified keywords against genre-specific keywords
    loaded beforehand from a file.

    Args:
        file_name (str): The file name where keywords are stored.
        user_keywords (list): A list of keywords specified by the user.

    Returns:
        tuple: A tuple containing the grade
        increment and the count of matched keywords.

    Raises:
        FileNotFoundError: If the file with pre-defined keywords is not found
        (spelling mistake / wrong constant)
    """
    try:
        with open(file_name, "r") as infile:
            file_keywords = infile.read().lower().split()
            grade_increment, keyword_count = 0, 0
            for user_keyword in user_keywords:
                for file_keyword in file_keywords:
                    if fuzz.ratio(user_keyword, file_keyword) >= 65:
                        # Uses fuzzy string matching to detect (close)
                        # keywords
                        grade_increment += 15
                        # Add points to the grade for each keyword found
                        keyword_count += 1
                        break
            return grade_increment, keyword_count
    except FileNotFoundError:
        print(
            f"No file with keywords found at {file_name}!"
            f"Please ensure such a file"
            f"exists before running the program "
            f"again!"
        )
        return 0


class Book:
    """
    Represents a book with attributes for title, author, price, year, and ISBN.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        price (float): The selling price of the book.
        year (int): The publication year of the book.
        isbn (str): The International Standard Book Number (ISBN).
    """

    def __init__(self, title, author, price, year, isbn):
        """
        Initializes a new instance of the Book class.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            price (float): Price of the book.
            year (int): Publication year of the book.
            isbn (str): ISBN of the book.
        """
        self.title = title
        self.author = author
        self.price = price
        self.year = year
        try:
            self.isbn = isbn
        except ValueError as ve:
            print(ve)
            sys.exit()

    @property
    def title(self):
        """Returns the title of the book."""
        return self._title

    @title.setter
    def title(self, new_title):
        """Sets the title of the book."""
        self._title = new_title

    @property
    def author(self):
        """Returns the author of the book."""
        return self._author

    @author.setter
    def author(self, new_author):
        """Sets the author of the book."""
        self._author = new_author

    @property
    def price(self):
        """Returns the price of the book."""
        return self._price

    @price.setter
    def price(self, new_price):
        """
        Sets the price of the book.
        Ensures that the price cannot be negative or zero;
        sets a default value if invalid.
        """
        self._price = new_price if new_price > 0 else 10

    @property
    def year(self):
        """Returns the publication year of the book."""
        return self._year

    @year.setter
    def year(self, new_year):
        """
        Sets the publication year of the book.
        Ensures the year is not negative or zero;
        sets a default value if invalid.
        """
        self._year = new_year if new_year > 0 else 2000

    @property
    def isbn(self):
        """Returns the ISBN of the book."""
        return self._isbn

    @isbn.setter
    def isbn(self, new_isbn):
        """
        Sets the ISBN of the book after validating its format.

        Args:
            new_isbn (str): The new ISBN to be set.

        Raises:
            ValueError: If the new ISBN does not match the expected format.
        """
        # Define the regex pattern for ISBN: four letters, a hyphen, then four
        # digits.
        pattern = r"^[A-Za-z]{4}-\d{4}$"
        if re.match(pattern, new_isbn):
            self._isbn = new_isbn
        else:
            raise ValueError(
                f"Invalid ISBN format: {new_isbn}."
                f"Expected format: 'AAAA-1234'."
            )

    @property
    def grade(self):
        """Returns the current grade of the book."""
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        """
        Sets the grade of the book.
        Ensures the grade is between 0 and 100.
        """
        self._grade = (
            new_grade
            if 0 <= new_grade <= 100
            else 100 if new_grade > 100 else 0
        )

    def get_genre(self):
        """
        Polymorphic method overridden in derived classes
        to return the genre of the book.

        Returns:
            str: The genre of the book.
        """
        pass

    def calculate_grade(self, book_criteria):
        """
        Calculates the initial grade of the book based on
        the price and external criteria.

        Args:
            book_criteria (BookCriteria): Criteria containing
            the maximum price acceptable and other factors.

        Returns: bool: True if it is safe to proceed
        with further grade modifications
        (i.e. if the price of the book
        is less than the maximum price specified by the user),
        otherwise False.
        """
        if self.price > book_criteria.max_price:
            self.grade = 0
            return False
        else:
            self.grade = 10
            return True

    def __lt__(self, other):
        """Compare this book instance with another
        book instance based on grade.

        Args:
            other (Book): The book instance to compare against.

        Returns: bool: True if this book's grade
        is less than the other book's grade,
        False otherwise or if the other
        is not an object of class Book.
        """
        if not isinstance(other, Book):
            print("Attempted to compare Book with non-Book type...")
            return False
        return self.grade < other.grade

    def __str__(self):
        """Provide a formatted string representation of the book instance.

        Returns:
            str: A string representing the book with title, author,
            publication year, price, ISBN, and grade.
        """
        return (
            f"{self.title} by {self.author}, published {self.year}."
            f" Genre: {self.get_genre()}. Price: {self.price}."
            f" ISBN: {self.isbn}. Grade: {self.grade}"
        )


class Fiction(Book):
    """Represents a fiction genre book, inheriting from Book."""

    pass


class NonFiction(Book):
    """Represents a non-fiction genre book, inheriting from Book."""

    pass
