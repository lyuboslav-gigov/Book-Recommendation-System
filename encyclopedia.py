"""
File: encyclopedia.py
Author: Lyuboslav Gigov
Purpose: Contains the Encyclopedia class, derived from NonFiction,
featuring methods to match books
with educational levels and to dynamically interact with the user
for specifying details about the needed encyclopedia.
"""

from book import NonFiction, match_keywords

KEYWORD_FILE_NAME = "Encyclopedia_Keywords.txt"


def validate_answer(answer):
    """
    Validates if the given answer is a valid response.

    Args:
        answer (str): The answer to validate.

    Returns:
        bool: True if the answer is 'yes' or 'no', False otherwise.
    """
    list_of_valid_answers = ["yes", "no"]
    if answer not in list_of_valid_answers:
        print("Please enter a valid answer (yes or no).")
        return False
    return True


def validate_level(level):
    """
    Validates if the given level is a valid educational level.

    Args:
        level (str): The educational level to validate.

    Returns:
        bool: True if the level is one of
        the predefined levels, False otherwise.
    """
    list_of_levels = [
        "middle school",
        "high school",
        "undergraduate",
        "graduate",
    ]
    if level not in list_of_levels:
        print(
            "Please enter a valid level"
            "(middle/high school, undergraduate/graduate)."
        )
        return False
    return True


class Encyclopedia(NonFiction):
    """
    Represents an encyclopedic book, inheriting from the NonFiction genre.

    This class is used to manage encyclopedic books and includes methods
    to match the book to an educational level.

    Attributes:
        prompted (bool): Class variable to check if
        the user has been prompted yet.
        user_needs_encyclopedia (bool): Class variable to check
        if the user needs an encyclopedia.
        education_level (str): Class variable to store
        the user's educational level preference.
    """

    prompted = False
    user_needs_encyclopedia = False
    education_level = ""

    def __init__(self, title, author, price, year, isbn):
        """
        Initialize the Encyclopedia instance with basic details.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            price (float): The price of the book.
            year (int): The publication year of the book.
            isbn (str): The ISBN of the book.
        """
        super().__init__(title, author, price, year, isbn)

    def get_genre(self):
        """
        Provides the genre of the book as 'Encyclopedia'.

        Returns:
            str: The genre of the book.
        """
        return "Encyclopedia"

    def matches_education_level(self, level):
        """
        Determines if the book matches the specified educational level.

        Args:
            level (str): The education level to match.

        Returns:
            bool: True if the book's title matches the expected
            title for the given level, False otherwise.
        """
        level_map = {
            "middle school": "The New Children's Encyclopedia",
            "high school": "World Encyclopedia for High School Students",
            "undergraduate": "Undergraduate Encyclopedia of Physics",
            "graduate": "Graduate Encyclopedia of Cosmology and Astrophysics",
        }
        return self.title == level_map.get(level, "")

    def calculate_grade(self, book_criteria):
        """
        Calculates the grade of the book based on user criteria
        and dynamic educational level matching.

        This method adjusts the grade of the book based on its match
        to an educational level if the user
        has expressed a need for an encyclopedia after dynamic interaction.

        Args:
            book_criteria (BookCriteria):The criteria
            against which to evaluate the book.
        """
        if super().calculate_grade(book_criteria):
            user_keywords = [word.lower() for word in book_criteria.info]

            if book_criteria.age < 10:
                self.grade = 0
                return

            _, keyword_count = match_keywords(KEYWORD_FILE_NAME, user_keywords)
            # Implement special dynamic interaction with the user
            # because they might need a very specific encyclopedia
            if keyword_count and not Encyclopedia.prompted:
                print(
                    "The search algorithm has detected that an"
                    " encyclopedic book might match your needs."
                )
                Encyclopedia.prompted = True
                while True:
                    answer = (
                        input("Is this correct (Yes/yes, No/no)? ")
                        .strip()
                        .lower()
                    )
                    if validate_answer(answer):
                        if answer == "yes":
                            Encyclopedia.user_needs_encyclopedia = True
                            while True:
                                Encyclopedia.education_level = (
                                    input(
                                        "For what level of education"
                                        " do you need it"
                                        " (middle school, high school,"
                                        "undergraduate, graduate)? "
                                    )
                                    .strip()
                                    .lower()
                                )
                                if validate_level(
                                    Encyclopedia.education_level
                                ):
                                    break
                            break
                        else:
                            print(
                                "Thank you for the feedback! Moving on "
                                "with the search ...\n"
                            )
                            break

            if Encyclopedia.user_needs_encyclopedia:
                # Check if this encyclopedia matches
                # the specified educational level
                if self.matches_education_level(Encyclopedia.education_level):
                    self.grade = 100
                else:
                    self.grade = 0  # Set to 0 if no match
                return  # Exit after handling
