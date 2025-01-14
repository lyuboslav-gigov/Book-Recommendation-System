"""
File: test_encyclopedia.py
Author: Lyuboslav Gigov
Purpose: This module contains unit tests for the Encyclopedia
class derived from NonFiction. It tests the initialization
of Encyclopedia instances to ensure all properties are correctly
set up according to the given values.
"""

import unittest
from encyclopedia import Encyclopedia


class TestEncyclopedia(unittest.TestCase):
    def setUp(self):
        self.book = Encyclopedia(
            "World Encyclopedia for High School Students",
            "Various Authors",
            29.99,
            2020,
            "ISBN" "-9999",
        )

    def test_initialization(self):
        self.assertEqual(
            self.book.title, "World Encyclopedia for High School Students"
        )
        self.assertEqual(self.book.author, "Various Authors")
        self.assertEqual(self.book.price, 29.99)
        self.assertEqual(self.book.year, 2020)
        self.assertEqual(self.book.isbn, "ISBN-9999")


if __name__ == "__main__":
    unittest.main()
