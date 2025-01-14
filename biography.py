"""
File: biography.py
Author: Lyuboslav Gigov
Purpose: Defines the Biography class that extends NonFiction.
This class includes specialized grading calculations based on
user keywords that match the biographical content.
"""

from book import NonFiction, match_keywords

KEYWORD_FILE_NAME = "Biography_Keywords.txt"


class Biography(NonFiction):
    """
    Represents a biography genre of books within a bookstore system,
    inheriting from NonFiction.

    Attributes:
        title (str): The title of the biography.
        author (str): The name of the author of the biography.
        price (float): The price of the biography.
        year (int): The publication year of the biography.
        isbn (str): The ISBN of the biography.
    """

    def __init__(self, title, author, price, year, isbn):
        """
        Constructs all the necessary attributes for the Biography object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            price (float): The price of the book.
            year (int): The year the book was published.
            isbn (str): The ISBN of the book.
        """
        super().__init__(title, author, price, year, isbn)

    def get_genre(self):
        """
        Provides the genre of the book as 'Biography'.

        Returns:
            str: The genre of the book.
        """
        return "Biography"

    def calculate_grade(self, book_criteria):
        """
        Calculates and updates the grade of the biography based on
        specific keywords and age criteria.

        This method specifically checks for keywords related to sports
        (like football, soccer, tennis)
        and adjusts the biography's grade to 100 if a match is found
        with the book's title. Otherwise, it
        increases the grade based on the age and increments
        the grade based on keywords found.

        Args: book_criteria (BookCriteria): An object of class BookCriteria
        containing criteria such as age, gender,
        maximum price the user is willing to pay and information
        for the specific requirements and preferences of the
        user.

        Returns:
            None: This method directly modifies the object's grade attribute.
        """
        if super().calculate_grade(book_criteria):
            grade_increment = 0
            user_keywords = [word.lower() for word in book_criteria.info]

            # These books require very specific keywords and characteristics
            if (
                any(k in user_keywords for k in ["football", "soccer"])
                and self.title == "Rafa: My Story"
            ):
                self.grade = 100
                return  # No need to go through the rest of the method
            elif (
                any(
                    kwrd in user_keywords
                    for kwrd in ["sports", "mentality", "relentless"]
                )
                and self.title
                == "Relentless: From Good to Great to Unstoppable"
            ):
                self.grade = 100
                return
            elif (
                "tennis" in user_keywords
                and self.title == "Open: An Autobiography"
            ):
                self.grade = 100
                return

            # Young people are inspired by biographies
            if 10 <= book_criteria.age <= 30:
                grade_increment += 25

            keyword_increment, _ = match_keywords(
                KEYWORD_FILE_NAME, user_keywords
            )
            grade_increment += keyword_increment
            self.grade += grade_increment
