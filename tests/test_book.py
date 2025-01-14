"""
File: test_book.py
Author: Lyuboslav Gigov
Purpose: This module contains unit tests for the Book class
and its subclasses Fiction and NonFiction.
It tests basic initialization, getter and setter methods,
boundary conditions for price and year,
grade calculations based on criteria, comparison operations,
and string representation.
The tests ensure that the Book class functions correctly
across a range of typical and edge case scenarios.
"""

import unittest
from io import StringIO
from unittest.mock import patch
from book import Book, Fiction, NonFiction
from book_criteria import BookCriteria


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(
            "Blah blah", "Peter Jackson", 12.34, 2000, "AAAA-1234"
        )

    def test_initialization(self):
        self.assertEqual(self.book.title, "Blah blah")
        self.assertEqual(self.book.author, "Peter Jackson")
        self.assertEqual(self.book.price, 12.34)
        self.assertEqual(self.book.year, 2000)
        self.assertEqual(self.book.isbn, "AAAA-1234")

    def test_getters_and_setters(self):
        self.book.title = "A Brief History of Mathematics"
        self.book.author = "Peter Dalakov"
        self.book.price = 29.99
        self.book.year = 2024

        self.assertEqual(self.book.title, "A Brief History of Mathematics")
        self.assertEqual(self.book.author, "Peter Dalakov")
        self.assertEqual(self.book.price, 29.99)
        self.assertEqual(self.book.year, 2024)

    def test_isbn_valid_format(self):
        valid_isbns = ["ABCD-1234", "WXYZ-5678", "abcd-9012", "wxyz-3456"]
        for isbn in valid_isbns:
            with self.subTest(isbn=isbn):
                self.book.isbn = isbn
                self.assertEqual(
                    self.book.isbn, isbn, f"Failed for ISBN: {isbn}"
                )

    def test_isbn_invalid_format_raises_value_error(self):
        invalid_isbns = [
            "ABCD1234",
            "1234-ABCD",
            "AB-123456",
            "ABCD-123",
            "1234-5678",
            "abcd-123",
        ]
        for isbn in invalid_isbns:
            with self.subTest(isbn=isbn):
                with self.assertRaises(ValueError) as context:
                    self.book.isbn = isbn
                self.assertIn(
                    "Invalid ISBN format",
                    str(context.exception),
                    f"Failed for ISBN: {isbn}",
                )

    def test_price_edge_cases(self):
        self.book.price = -100
        self.assertEqual(self.book.price, 10)

        self.book.price = 0
        self.assertEqual(self.book.price, 10)

    def test_year_edge_cases(self):
        self.book.year = -100
        self.assertEqual(self.book.year, 2000)

        self.book.year = 0
        self.assertEqual(self.book.year, 2000)

    def test_calculate_grade_valid_criteria(self):
        criteria = BookCriteria(max_price=25)
        self.book.calculate_grade(criteria)
        self.assertEqual(self.book.grade, 10)

    def test_calculate_grade_price_too_high(self):
        criteria = BookCriteria(max_price=10)
        self.book.calculate_grade(criteria)
        self.assertEqual(self.book.grade, 0)

    def test_lt_operator(self):
        other_book = Book(
            "Other Book", "Another Author", 30.0, 2018, "HAHA-0001"
        )
        criteria = BookCriteria(max_price=30)

        self.book.calculate_grade(criteria)
        other_book.calculate_grade(criteria)

        self.assertFalse(self.book < other_book)

    def test_string_representation(self):
        criteria = BookCriteria(max_price=29.99)
        self.book.calculate_grade(criteria)

        expected_str = ("Blah blah by Peter Jackson, published 2000."
                        " Genre: None."
                        " Price: 12.34. ISBN: AAAA-1234. Grade: 10")
        self.assertEqual(str(self.book), expected_str)

    def test_fiction_subclass(self):
        fiction_book = Fiction(
            "Fiction Book", "Fiction Author", 15.0, 2010, "LOLO-9999"
        )
        self.assertTrue(isinstance(fiction_book, Fiction))
        self.assertTrue(isinstance(fiction_book, Book))

    def test_nonfiction_subclass(self):
        nonfiction_book = NonFiction(
            "NonFiction Book",
            "NonFiction Author",
            25.0,
            2005,
            "ABCD-1991",
        )
        self.assertTrue(isinstance(nonfiction_book, NonFiction))
        self.assertTrue(isinstance(nonfiction_book, Book))


if __name__ == "__main__":
    unittest.main()
