"""
File: romance.py
Author: Lyuboslav Gigov
Purpose: This module defines the Romance class, a subclass of Fiction,
incorporating elements like emotional depth and realism
to align book recommendations with user mood preferences.
"""

from book import Fiction, match_keywords

KEYWORD_FILE_NAME = "Romance_Keywords.txt"


def validate_mood(mood):
    """
    Checks if the specified mood is valid.

    Args:
        mood (str): The mood to validate.

    Returns:
        bool: True if the mood is valid, False otherwise.
    """
    list_of_moods = ["happy", "sad", "adventurous", "need a laugh"]
    if mood not in list_of_moods:
        return False
    return True


def get_mood():
    """
    Prompts the user to enter their current mood and validates it.

    Returns:
        str: The validated mood of the user.
    """
    while True:
        mood = input(
            "How are you feeling today "
            "(happy, sad, adventurous, need a laugh)? "
        )
        if validate_mood(mood):
            return mood


class Romance(Fiction):
    """
    Represents a Romance genre book with specific attributes
    related to emotional depth and realism.

    Attributes:
        prompted (bool): Class variable to check if the user
        has been prompted about their mood.
        user_wants_romance (bool): Class variable to check if the user
        wants a romance book recommendation.
        user_mood (str): Class variable to store the user's mood
        for recommending a romance book.
        emotional_depth (int): Represents the emotional depth of
        the romance narrative, from 0 to 100.
        realism (int): Represents the level of realism
        in the romance narrative, from 0 to 100.
        title (str): The title of the biography.
        author (str): The name of the author of the biography.
        price (float): The price of the biography.
        year (int): The publication year of the biography.
        isbn (str): The ISBN of the biography.
    """
    # Static class variable to signify whether user has been prompted or not
    prompted = False
    user_wants_romance = False
    user_mood = "need a laugh"  # Default value

    def __init__(
        self, title, author, price, year, isbn, emotional_depth, realism
    ):
        """
        Initializes a Romance book with additional
        attributes for emotional depth and realism.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            price (float): The price of the book.
            year (int): The publication year of the book.
            isbn (str): The ISBN of the book.
            emotional_depth (int): A measure of the
            emotional depth of the book.
            realism (int): A measure of how realistically
            the book portrays its themes.
        """
        super().__init__(title, author, price, year, isbn)
        self.emotional_depth = emotional_depth
        self.realism = realism

    @property
    def emotional_depth(self):
        """
        Gets the emotional depth of the book.

        Returns:
            int: The emotional depth value.
        """
        return self._emotional_depth

    @emotional_depth.setter
    def emotional_depth(self, new_val):
        """
        Sets the emotional depth of the book.
        Ensures the value is between 0 and 100.

        Args:
            new_val (int): The new value for emotional depth.
        """
        self._emotional_depth = (
            0 if new_val < 0 else 100 if new_val > 100 else new_val
        )

    @property
    def realism(self):
        """
        Gets the realism level of the book.

        Returns:
            int: The realism level value.
        """
        return self._realism

    @realism.setter
    def realism(self, new_val):
        """
        Sets the realism level of the book.
        Ensures the value is between 0 and 100.

        Args:
            new_val (int): The new value for realism.
        """
        self._realism = 0 if new_val < 0 else 100 if new_val > 100 else new_val

    def get_genre(self):
        """
        Provides the genre of the book as 'Romance'.

        Returns:
            str: The genre of the book.
        """
        return "Romance"

    def matches_mood_to_book(self, mood):
        """
        Matches the user's mood to a specific romance book.

        Args:
            mood (str): The user's mood.

        Returns:
            bool: True if the book matches the user's mood, False otherwise.
        """
        mood_map = {
            "happy": "Me Before You",
            "sad": "The Fault in Our Stars",
            "adventurous": "Outlander",
            "need a laugh": "Can You Keep a Secret?",
        }
        return self.title == mood_map.get(mood, "")

    def base_grade(self, book_criteria):
        """
        Computes the base grade of the book based on multiple
        criteria including user demographics and book attributes.

        Args:
            book_criteria (BookCriteria): The criteria
            against which to evaluate the book.

        Returns:
            float: The computed base grade for the book.
        """
        age_weight, emotional_depth_weight, realism_weight, gender_weight = (
            0.1,
            0.1,
            0.1,
            0.1,
        )
        age_relevance = (
            100
            if 10 <= book_criteria.age <= 20
            else 80 if 20 < book_criteria.age <= 30 else 60
        )
        gender_relevance = (
            100
            if book_criteria.gender == "woman"
            else 80 if book_criteria.gender == "man" else 60
        )
        return (
            age_weight * age_relevance
            + emotional_depth_weight * self.emotional_depth
            + realism_weight * self.realism
            + gender_weight * gender_relevance
        )

    def calculate_grade(self, book_criteria):
        """
        Calculates and updates the grade of the book
        based on the user's criteria and mood.

        Args:
            book_criteria (BookCriteria): The criteria
            against which to evaluate the book.

        Returns:
            None: The method directly modifies the grade property of the book.
        """
        if super().calculate_grade(book_criteria):
            user_keywords = [word.lower() for word in book_criteria.info]
            initial_grade = self.base_grade(book_criteria)
            self.grade += initial_grade

            _, keyword_count = match_keywords(KEYWORD_FILE_NAME, user_keywords)

            if keyword_count and not Romance.prompted:
                Romance.prompted = True
                Romance.user_wants_romance = True
                Romance.user_mood = get_mood()

            if Romance.user_wants_romance:
                if self.matches_mood_to_book(Romance.user_mood):
                    self.grade += 40
                    print(
                        f"\nBased on your mood, we recommend "
                        f"{self.title} by {self.author}.\n"
                    )
