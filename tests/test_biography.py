"""
File: test_biography.py
Author: Lyuboslav Gigov
Purpose: This module contains unit tests for the Biography class,
ensuring proper initialization and behavior.
It tests attributes like title, author, price, year, and ISBN
to ensure they are set correctly upon instantiation.
Additional tests can be added to verify methods
and functionality specific to the Biography class.
"""

import unittest
from biography import Biography


class TestBiography(unittest.TestCase):
    def setUp(self):
        self.biography = Biography(
            "Rafa: My Story", "Rafael Nadal", 12.99, 2011, "KKKO-1313"
        )

    def test_initialization(self):
        self.assertEqual(self.biography.title, "Rafa: My Story")
        self.assertEqual(self.biography.author, "Rafael Nadal")
        self.assertEqual(self.biography.price, 12.99)
        self.assertEqual(self.biography.year, 2011)
        self.assertEqual(self.biography.isbn, "KKKO-1313")


if __name__ == "__main__":
    unittest.main()
