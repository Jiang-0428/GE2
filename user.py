## This module contains the user interface for the library system. 
# It allows users to search for books, borrow books, and return books.

## Import the necessary functions from the admin module. 
# Replace "function_name1" with the actual function names you want to import.
from admin import (
    load_library,
    save_library,
    find_book
)




## Search books by category.
## This function should return book IDs that match the given category.
def books_in_category(
    books,
    category
):
    clean_input = category.strip().lower()
    matched_ids = []
    for book_id, book_data in books.items():
        if book_data["category"].lower() == clean_input:
            matched_ids.append(book_id)
    return matched_ids

    


## Search books by full or partial title.
## This function should return book IDs that match the given title or part of the title.
def search_by_title(
    books,
    search_text
):
    clean_text = search_text.lower()
    matches = []
    for bid, info in books.items():
        if clean_text in info["title"].lower():
            matches.append(bid)
    return matches
    


## Create logic to let users borrow books.
## The function should check if the book is available or on loan, or if the borrower name is provided.
## If the book is not found, then return "BOOK_NOT_FOUND"
## If the borrower name is empty, then return "EMPTY_NAME"
## If the book is not available, then return "NOT_AVAILABLE"
## If the book is successfully borrowed, then return "OK"
def borrow_book(
    books,
    loans,
    search_text,
    borrower
):
    clean_borrower = borrower.strip()
    if not clean_borrower:
        return "EMPTY_NAME"

    book_id = find_book(books, search_text)
    if book_id is None:
        return "BOOK_NOT_FOUND"

    book = books[book_id]
    if not book["available"]:
        return "NOT_AVAILABLE"

    book["available"] = False
    loans.append({"book_id": book_id, "borrower": clean_borrower})
    return "OK"

    


## Create logic to let users return books.
## The function should check if the book is on loan, or if the borrower name is provided
## If the book is not found, then return "BOOK_NOT_FOUND"
## If the borrower name is empty, then return "EMPTY_NAME"
## If the book is not on loan, then return "NOT_ON_LOAN"
## If the book is successfully returned, then return "OK"

def return_book(
    books,
    loans,
    book_title,
    borrower
):
    clean_borrower = borrower.strip()
    if not clean_borrower:
        return "EMPTY_NAME"

    book_id = find_book(books, book_title)
    if book_id is None:
        return "BOOK_NOT_FOUND"

    loan_index = None
    for idx, loan in enumerate(loans):
        if loan["book_id"] == book_id:
            loan_index = idx
            break
    if loan_index is None:
        return "NOT_ON_LOAN"

    del loans[loan_index]
    books[book_id]["available"] = True
    return "OK"

    



## The main function that runs the user interface for the library system.
## The function must first load the library data from a JSON file, then display a menu for the user to select options.
## The options include searching for books by title or category, borrowing a book, returning a book, and exiting the program.
## When the user selects an option, the corresponding function is called to perform the action.
## The program continues to display the menu until the user chooses to exit, at which point the library data is saved back to the JSON file.
## The main function should also handle invalid selections by displaying an error message and prompting the user to select again.
def main():
    data = load_library("library.json")
    books = data["books"]
    loans = data["loans"]
    filename = "library.json"

    print("LIBRARY USER SYSTEM")
    while True:
        print("\n==== MENU ====")
        print("1. Search books by title")
        print("2. Search books by category")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your selection: ")

        if choice == "1":
            text = input("Enter title (partial ok): ")
            ids = search_by_title(books, text)
            print("Matching book IDs:", ids)
        elif choice == "2":
            cat = input("Enter category: ")
            ids = books_in_category(books, cat)
            print("Matching book IDs:", ids)
        elif choice == "3":
            search_txt = input("Enter book ID / title / author to borrow: ")
            bor_name = input("Enter borrower name: ")
            res = borrow_book(books, loans, search_txt, bor_name)
            print("Result:", res)
        elif choice == "4":
            search_txt = input("Enter book ID / title / author to return: ")
            bor_name = input("Enter borrower name: ")
            res = return_book(books, loans, search_txt, bor_name)
            print("Result:", res)
        elif choice == "5":
            save_library(data, filename)
            print("Saved data, exiting.")
            break
        else:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    main()

