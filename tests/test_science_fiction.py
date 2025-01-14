"""
File: test_science_fiction.py
Author: Lyuboslav Gigov
Purpose: This module contains unit tests for the ScienceFiction class,
which is a subclass of Fiction.
It verifies that the ScienceFiction class correctly
initializes with provided attributes,
and that its setters for scientific_accuracy and
action_level correctly handle values outside their intended range.
"""

import unittest
from science_fiction import ScienceFiction


class TestScienceFiction(unittest.TestCase):
    def setUp(self):
        self.book = ScienceFiction(
            "Neuromancer", "William Gibson", 15.99, 1984, "ABCD-3456", 90, 80
        )

    def test_initialization(self):
        self.assertEqual(self.book.title, "Neuromancer")
        self.assertEqual(self.book.author, "William Gibson")
        self.assertEqual(self.book.price, 15.99)
        self.assertEqual(self.book.year, 1984)
        self.assertEqual(self.book.isbn, "ABCD-3456")
        self.assertEqual(self.book.scientific_accuracy, 90)
        self.assertEqual(self.book.action_level, 80)

    def test_scientific_accuracy_setter(self):
        self.book.scientific_accuracy = 105
        self.assertEqual(self.book.scientific_accuracy, 100)
        self.book.scientific_accuracy = -10
        self.assertEqual(self.book.scientific_accuracy, 0)

    def test_action_level_setter(self):
        self.book.action_level = 105
        self.assertEqual(self.book.action_level, 100)
        self.book.action_level = -5
        self.assertEqual(self.book.action_level, 0)


if __name__ == "__main__":
    unittest.main()
