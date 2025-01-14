"""
File: science_fiction.py
Author: Lyuboslav Gigov
Purpose: This module defines the ScienceFiction class,
which extends the Fiction class and includes properties
and methods specific to science fiction books,
such as handling scientific accuracy and action levels.
"""

from book import Fiction, match_keywords

KEYWORD_FILE_NAME = "Science_Fiction_Keywords.txt"


class ScienceFiction(Fiction):
    """
    Represents a science fiction genre book with additional
    attributes for scientific accuracy and action level.

    Attributes:
        title (str): The title of the biography.
        author (str): The name of the author of the biography.
        price (float): The price of the biography.
        year (int): The publication year of the biography.
        isbn (str): The ISBN of the biography.
        scientific_accuracy (int): Measures how scientifically accurate
        the contents are, scaled 0-100.
        action_level (int): Indicates the intensity of
        action content in the book, scaled 0-100.
    """

    def __init__(
        self,
        title,
        author,
        price,
        year,
        isbn,
        scientific_accuracy,
        action_level,
    ):
        """
        Initializes a Science Fiction book with additional attributes
        for scientific accuracy and action level.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            price (float): The price of the book.
            year (int): The publication year of the book.
            isbn (str): The ISBN of the book.
            scientific_accuracy (int): A measure of the
            scientific accuracy of the book's content.
            action_level (int): A measure of the
            intensity of action in the book.
        """
        super().__init__(title, author, price, year, isbn)
        self.scientific_accuracy = scientific_accuracy
        self.action_level = action_level

    @property
    def scientific_accuracy(self):
        """
        Gets the scientific accuracy level of the book.

        Returns:
            int: The scientific accuracy level.
        """
        return self._scientific_accuracy

    @scientific_accuracy.setter
    def scientific_accuracy(self, new_val):
        """
        Sets the scientific accuracy of the book.
        Ensures the value is between 0 and 100.

        Args:
            new_val (int): The new value for scientific accuracy.
        """
        if new_val < 0:
            self._scientific_accuracy = 0
        elif new_val > 100:
            self._scientific_accuracy = 100
        else:
            self._scientific_accuracy = new_val

    @property
    def action_level(self):
        """
        Gets the action level of the book.

        Returns:
            int: The action level.
        """
        return self._action_level

    @action_level.setter
    def action_level(self, new_val):
        """
        Sets the action level of the book.
        Ensures the value is between 0 and 100.

        Args:
            new_val (int): The new value for action level.
        """
        self._action_level = (
            0 if new_val < 0 else 100 if new_val > 100 else new_val
        )

    def get_genre(self):
        """
        Provides the genre of the book as 'Science Fiction'.

        Returns:
            str: The genre of the book.
        """
        return "Science Fiction"

    def calculate_grade(self, book_criteria):
        """
        Calculates and updates the grade of the book based on
        the specified book criteria and inherent book properties.

        Args:
            book_criteria (BookCriteria): An object
            containing criteria to grade the book.

        Returns:
            None: The method directly modifies
            the grade property of the book.
        """
        if super().calculate_grade(book_criteria):
            user_keywords = [word.lower() for word in book_criteria.info]

            # Sci-fi enthusiasts might be looking for specific themes
            if any(
                k in user_keywords
                for k in ["space", "ai", "robotics", "future"]
            ) and self.title in ["Neuromancer", "Dune"]:
                self.grade = 100
                return

            # Grade calculation based on multiple factors
            # grade = weight1 * relevance1 + weight2 * relevance2 + ...
            (
                weight_age,
                weight_gender,
                weight_sc_accuracy,
                weight_action_level,
            ) = (0.1, 0.1, 0.1, 0.1)
            age_relevance = (
                80
                if book_criteria.age <= 18
                else 100 if 18 < book_criteria.age < 35 else 60
            )
            gender_relevance = (
                100
                if book_criteria.gender == "man"
                else 80 if book_criteria.gender == "woman" else 70
            )

            keyword_increment, keyword_count = match_keywords(
                KEYWORD_FILE_NAME, user_keywords
            )
            self.grade += (
                weight_age * age_relevance
                + weight_gender * gender_relevance
                + weight_sc_accuracy * self.scientific_accuracy
                + weight_action_level * self.action_level
                + keyword_increment
            )
