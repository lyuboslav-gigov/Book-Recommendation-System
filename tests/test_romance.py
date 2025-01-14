"""
File: test_romance.py
Author: Lyuboslav Gigov
Purpose: This module contains unit tests for
the Romance class, a subclass of Fiction.
It focuses on testing initialization,
setter methods for emotional depth and realism,
and correct adjustments to these properties
when set with valid and invalid
values. Additional complex interaction tests for grade calculation
based on user criteria and mood are commented out.
"""

import unittest
from romance import Romance


class TestRomance(unittest.TestCase):
    def setUp(self):
        self.book = Romance(
            "Me Before You", "Jojo Moyes", 15.99, 2012, "ISBN-1234", 90, 85
        )

    def test_initialization(self):
        self.assertEqual(self.book.title, "Me Before You")
        self.assertEqual(self.book.author, "Jojo Moyes")
        self.assertEqual(self.book.price, 15.99)
        self.assertEqual(self.book.year, 2012)
        self.assertEqual(self.book.isbn, "ISBN-1234")
        self.assertEqual(self.book.emotional_depth, 90)
        self.assertEqual(self.book.realism, 85)

    def test_emotional_depth_setter(self):
        self.book.emotional_depth = 105
        self.assertEqual(self.book.emotional_depth, 100)
        self.book.emotional_depth = -10
        self.assertEqual(self.book.emotional_depth, 0)
        self.book.emotional_depth = 89
        self.assertEqual(self.book.emotional_depth, 89)

    def test_realism_setter(self):
        self.book.realism = 110
        self.assertEqual(self.book.realism, 100)
        self.book.realism = -5
        self.assertEqual(self.book.realism, 0)
        self.book.realism = 75
        self.assertEqual(self.book.realism, 75)


if __name__ == "__main__":
    unittest.main()
