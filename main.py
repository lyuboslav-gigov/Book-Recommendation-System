"""
File: main.py
Author: Lyuboslav Gigov
Purpose: Entry point of the application that integrates all modules to
provide book recommendations
based on user preferences captured through an interactive session.
Final output is shown in tabulated form for clarity and readability.
"""

from book_criteria import BookCriteria
from bookstore import Bookstore
from tabulate import tabulate


def validate_gender(gender):
    """Validate the user's input for gender.

    Args:
        gender (str): The gender entered by the user.

    Returns:
        bool: True if the gender is valid, False otherwise.
    """
    list_of_valid_genders = ["man", "woman", "other"]
    if gender.lower() not in list_of_valid_genders:
        print("Please enter a valid gender (man, woman, or other).")
        return False
    return True


def get_user_preferences():
    """Interactively collect user preferences for book selection.

    Returns:
        BookCriteria: An instance of BookCriteria
        containing the user's preferences.
    """
    print("Hello! This program will help you choose the ideal book"
          " based on your age, gender, hobbies, and interests.")

    # Loop until a valid age is entered
    while True:
        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Please enter a positive number for age.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")

    # Loop until a valid maximum price is entered
    while True:
        try:
            max_price = float(input("Enter max price (in US $): "))
            if max_price <= 0:
                print("Please enter a positive number for maximum price.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a "
                  "valid number for maximum price.")

    # Loop until a valid gender is entered
    while True:
        gender = input("Enter gender: ").strip()
        if validate_gender(gender):
            break

    info = input(
        "Tell me what type of book you want to buy "
        "(romance, fantasy, sci-fi, etc.),"
        " what you need it for ("
        "leisure, gift, studying),\nwhat are some of your interests"
        " (sport, science, technology). You can "
        "enter just several keywords or several sentences:\n").split()
    return BookCriteria(age, max_price, gender, info)


def sort_books(books):
    """Sort a list of books in descending order based on their grade attribute.

    Args:
        books (list): A list of Book instances to be sorted.
    """
    books.sort(reverse=True)  # Uses the overloaded __lt__ method


def main():
    """Main function to run the bookstore application."""
    my_bookstore = Bookstore()
    book_collection = my_bookstore.load_books()
    user_criteria = get_user_preferences()

    for book in book_collection:
        book.calculate_grade(user_criteria)

    # Sort the books by grade in descending order
    sort_books(book_collection)

    # Converting books to dictionaries to easily display them in a tabular form
    books_data = [{
        "No.": index,
        "Title": book.title,
        "Author": book.author,
        "Year": book.year,
        "Genre": book.get_genre(),
        "Price": f"${book.price:.2f}",
        "ISBN": book.isbn,
        "Grade": f"{book.grade}/100"
    } for index, book in enumerate(book_collection[:5], 1)]

    print("\nThe five most suitable books for you are:\n")
    print(tabulate(books_data, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
