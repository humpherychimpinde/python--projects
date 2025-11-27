import json
import os
from datetime import datetime

# FILE HANDLING

FILE_NAME = "library.json"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

# Load books
def load_books():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save books
def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)


# BACKEND FUNCTIONS

#  ADD BOOK RECORD
def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year Published: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "status": "Available",
        "borrower": "",
        "date_borrowed": "",
        "student_number": "",
        "duration": ""
    }

    books.append(book)
    save_books(books)
    print("\nBook added successfully.\n")


#  VIEW ALL BOOKS
def view_books():
    books = load_books()

    if not books:
        print("\nNo books found.\n")
        return

    print("\n======= ALL BOOKS =======")
    for book in books:
        print(f"""
ID: {book.get('id')}
Title: {book.get('title')}
Author: {book.get('author')}
Year: {book.get('year')}
Status: {book.get('status')}
Borrower: {book.get('borrower', 'None')}
Date Borrowed: {book.get('date_borrowed', 'None')}
Student_Number: {book.get('student_number', 'None')}
Duration: {book.get('duration', 'None')}
------------------------------""")
    print()


#  SEARCH BOOK BY ID OR TITLE
def search_book():
    books = load_books()
    search_key = input("Enter Book ID or Title to search: ").lower()

    for book in books:
        if search_key == book["id"].lower() or search_key == book["title"].lower():
            print("\nBOOK FOUND")
            print(f"""
ID: {book['id']}
Title: {book['title']}
Author: {book['author']}
Year: {book['year']}
Status: {book['status']}
Borrower: {book['borrower']}
Date Borrowed: {book['date_borrowed']}
Student Number: {book['student_number']}
Duration: {book['duration']}
""")
            return

    print("\nBook not found.\n")


#  BORROW BOOK
def borrow_book():
    books = load_books()
    book_id = input("Enter Book ID to borrow: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Borrowed":
                print("\nBook is already borrowed.\n")
                return

            borrower = input("Enter borrower's name: ")
            date_borrowed = datetime.now().strftime("%Y-%m-%d")
            student_id = input("Enter student_number: ")
            duration = input("Enter duration (days):")

            book["status"] = "Borrowed"
            book["borrower"] = borrower
            book["date_borrowed"] = date_borrowed
            book["student_number"] = student_id
            book["duration"] = duration
            save_books(books)
            print("\nBook borrowed successfully.\n")
            return

    print("\nBook not found.\n")


#  RETURN BOOK
def return_book():
    books = load_books()
    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book.get("id") == book_id:
            if book.get("status","Available") == "Available":
                print("\nBook is not borrowed.\n")
                return
            borrower_name = book.get("borrower", "Unknown")
            date_borrowed = book.get("date_borrowed", "Unknown")
# Show borrower info before clearing it 
            print(f"\nBook was borrowed by: {borrower_name}")
            print(f"Date borrowed: {date_borrowed}")
            book["status"] = "Available"
            book["borrower"] = ""
            book["date_borrowed"] = ""

            save_books(books)
            print("\nBook returned successfully.\n")
            return

    print("\nBook not found.\n")


#  DELETE BOOK RECORD
def delete_book():
    books = load_books()
    search_key = input("Enter Book ID or Title to delete: ").lower()

    for book in books:
        if search_key == book["id"].lower() or search_key == book["title"].lower():
            books.remove(book)
            save_books(books)
            print("\nBook deleted successfully.\n")
            return

    print("\nBook not found.\n")

def menu():
    while True:
        print("""
======== ROCKVIEW UNIVERSITY LIBRARY MANAGEMENT SYSTEM ========

1. Add Book
2. View All Books
3. Search Book
4. Borrow Book
5. Return Book
6. Delete Book
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("\nExiting system... Goodbye.\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")


# RUN SYSTEM
menu()
