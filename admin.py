##Import the necessary module
import json


## This function should load the library data from a JSON file and return it as a suitable Python data structure.
def load_library(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


## This function should save the library data to a JSON file.
## This function does not need to return anything, but it should ensure that the data is saved correctly to the specified file.
def save_library(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    



## This function should find a book by its title, author, or ID.
## If the book is found, it should return the book ID.
## If the book is not found, it should return None.
def find_book(books, search_text):
    clean_search = search_text.strip().lower()
    for book_id, book_info in books.items():
        if book_id.lower() == clean_search:
            return book_id
        if book_info["title"].lower() == clean_search:
            return book_id
        if book_info["author"].lower() == clean_search:
            return book_id
    return None



## This function should display the list of books in a user-friendly format.
## It should show the book ID, title, category, and availability status (available or on loan).
## If the book is available, it should display "AVAILABLE", and if it is on loan, it should display "ON LOAN".
## The function should not return anything, but it should print the information to the console.
## The heading for this display should be "BOOK CATALOGUE".
def display_books(books):
    print("BOOK CATALOGUE")
    print("-" * 60)
    for book_id, book in books.items():
        status = "AVAILABLE" if book["available"] else "ON LOAN"
        print(f"{book_id} | {book['title']} | {book['category']} | {status}")


## This function should display the list of current loans in a user-friendly format.
## It should show the book ID, title, and the name of the borrower.
## The heading for this display should be "CURRENT LOANS".
## The function should not return anything, but it should print the information to the console.
def display_loans(loans, books):
    print("CURRENT LOANS")
    print("-" * 60)
    for loan in loans:
        bid = loan["book_id"]
        borrower = loan["borrower"]
        title = books[bid]["title"]
        print(f"{bid} | {title} | Borrower: {borrower}")


## This function should calculate and return the library statistics
## The statsitics should include the total number of books, the number of available books, and the number of borrowed books.
## The function should return these three values in the order: total, available, borrowed. Use a suitable data structure to return these values, such as a tuple or a dictionary.

def library_statistics(books):
    total = len(books)
    available = sum(1 for b in books.values() if b["available"])
    borrowed = total - available
    return (total, available, borrowed)


## This function should display the library statistics in a user-friendly format.
## It should first load the library data from a JSON file, 
## Then calculate the statistics, and finally print the information to the console.
## The heading for this display should be "LIBRARY STATISTICS".
## It should print the total number of books, the number of available books, and the number of borrowed books.
## The function should not return anything, but it should print the information to the console.
def main():
    data = load_library("library.json")
    lib_info = data["library"]
    categories = data["categories"]
    books = data["books"]
    loans = data["loans"]


## Following is how the Admin interface should look like when the program is run. 
# The actual output may vary based on the library data and the current state of loans.

""" 
LIBRARY ADMINISTRATION
============================================================
Library: 
Branch: 
Year: 
Categories: 

BOOK CATALOGUE
------------------------------------------------------------
ID1 | Title1 | Category | Availability
ID2 | Title2 | Category | Availability
...
...
...
IDN | TitleN | Category | Availability


CURRENT LOANS
------------------------------------------------------------
ID1 | Title1 | Borrower: Borrower1
ID2 | Title2 | Borrower: Borrower2
...
...
...
IDN | TitleN | Borrower: BorrowerN

STATISTICS
------------------------------------------------------------
Total books: XX
Available: XX
Borrowed: XX
"""

def load_library(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def save_library(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def find_book(books, search_text):
    clean_search = search_text.strip().lower()
    for book_id, book_info in books.items():
        if book_id.lower() == clean_search:
            return book_id
        if book_info["title"].lower() == clean_search:
            return book_id
        if book_info["author"].lower() == clean_search:
            return book_id
    return None

def display_books(books):
    print("BOOK CATALOGUE")
    print("-" * 60)
    for book_id, book in books.items():
        status = "AVAILABLE" if book["available"] else "ON LOAN"
        print(f"{book_id:<4} | {book['title']:<25} | {book['category']:<15} | {status}")

def display_loans(loans, books):
    print("CURRENT LOANS")
    print("-" * 60)
    for loan in loans:
        bid = loan["book_id"]
        borrower = loan["borrower"]
        title = books[bid]["title"]
        print(f"{bid:<4} | {title:<25} | Borrower: {borrower}")

def library_statistics(books):
    total = len(books)
    available = sum(1 for b in books.values() if b["available"])
    borrowed = total - available
    return (total, available, borrowed)

def main():
    data = load_library("library.json")
    lib_info = data["library"]
    categories = data["categories"]
    books = data["books"]
    loans = data["loans"]

    print("LIBRARY ADMINISTRATION")
    print("=" * 60)
    print(f"Library: {lib_info['name']}")
    print(f"Branch: {lib_info['branch']}")
    print(f"Year: {lib_info['year']}")
    print(f"Categories: {', '.join(categories)}")

    display_books(books)
    print()
    display_loans(loans, books)
    print()
    print("STATISTICS")
    print("-" * 60)
    total, avail, bor = library_statistics(books)
    print(f"Total books: {total}")
    print(f"Available: {avail}")
    print(f"Borrowed: {bor}")

if __name__ == "__main__":
    main()