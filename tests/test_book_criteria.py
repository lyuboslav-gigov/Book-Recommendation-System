"""
File: test_book_criteria.py
Author: Lyuboslav Gigov
Purpose: This module contains unit tests for the BookCriteria class.
It validates initialization, property setters
and getters, and the proper string representation
of BookCriteria instances.
The tests confirm that BookCriteria can store
and return user preferences accurately.
"""

import unittest
from book_criteria import BookCriteria


class TestBookCriteria(unittest.TestCase):
    def setUp(self):
        self.criteria = BookCriteria(
            22, 50, "man", "I like watching football and drinking beer!"
        )

    def test_initialization(self):
        self.assertEqual(self.criteria.age, 22)
        self.assertEqual(self.criteria.max_price, 50)
        self.assertEqual(self.criteria.gender, "man")
        self.assertEqual(
            self.criteria.info, "I like watching football and drinking beer!"
        )

    def test_property_setters_and_getters(self):
        new_criteria = BookCriteria()
        new_criteria.age = 28
        new_criteria.max_price = 59.99
        new_criteria.gender = "other"
        new_criteria.info = "Poker and rugby are my two passions"

        self.assertEqual(new_criteria.age, 28)
        self.assertEqual(new_criteria.max_price, 59.99)
        self.assertEqual(new_criteria.gender, "other")
        self.assertEqual(
            new_criteria.info, "Poker and rugby are my two passions"
        )

    def test_string_representation(self):
        criteria = BookCriteria()
        expected_str = ("Age: 18, Max Price: 100, Gender: woman, "
                        "Info: I am looking for an interesting sci-fi book "
                        "to read for leisure at home")
        self.assertEqual(str(criteria), expected_str)


if __name__ == "__main__":
    unittest.main()
