"""
File: book_criteria.py
Author: Lyuboslav Gigov
Purpose: This file includes the BookCriteria class,
which encapsulates criteria such as age, price, gender,
and user information that are used across various book classes
to determine the suitability of books.
"""


class BookCriteria:
    """Represents the criteria for selecting a book based on user preferences.

    Attributes:
        age (int): The age of the user to tailor book recommendations.
        max_price (float): The maximum price the user
        is willing to pay for a book.
        gender (str): The gender of the user for
        potentially tailored recommendations.
        info (str): Additional information or
        preferences expressed by the user.
    """

    def __init__(
        self,
        age=18,
        max_price=100,
        gender="woman",
        info="I am looking for an interesting sci-fi book to "
        "read for leisure at home",
    ):
        """Initialize the BookCriteria instance with
        default values or provided values.

        Args:
            age (int): The user's age, defaults to 18.
            max_price (float): The maximum price the user is
            willing to pay, defaults to 100.
            gender (str): The user's gender, defaults to 'woman'.
            info (str): Additional information about user preferences,
            defaults to a generic interest in sci-fi.
        """
        self.age = age
        self.max_price = max_price
        self.gender = gender
        self.info = info

    # No validations needed for the properties because get_user_preferences()
    # in main.py ensures the user enters valid
    # input
    @property
    def age(self):
        """Get the user's age."""
        return self._age

    @age.setter
    def age(self, new_age):
        """Set the user's age.

        Args:
            new_age (int): The new age to set.
        """
        self._age = new_age

    @property
    def max_price(self):
        """Get the maximum price the user is willing to pay."""
        return self._max_price

    @max_price.setter
    def max_price(self, new_max_price):
        """Set the maximum price the user is willing to pay.

        Args:
            new_max_price (float): The new maximum price to set.
        """
        self._max_price = new_max_price

    @property
    def gender(self):
        """Get the user's gender."""
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        """Set the user's gender.

        Args:
            new_gender (str): The new gender to set.
        """
        self._gender = new_gender

    @property
    def info(self):
        """Get the additional information or
        preferences expressed by the user."""
        return self._info

    @info.setter
    def info(self, new_info):
        """Set the additional information or preferences expressed by the user.

        Args:
            new_info (str): The new information to set.
        """
        self._info = new_info

    def __str__(self):
        """Return a string representation of the book criteria."""
        return (f"Age: {self.age}, Max Price: {self.max_price},"
                f" Gender: {self.gender}, Info: {self.info}")
