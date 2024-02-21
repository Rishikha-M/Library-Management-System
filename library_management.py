# library_management.py

import csv
import getpass

# File path for storing book data
BOOKS_FILE = "books.csv"

# Function to load books from CSV file
def load_books():
    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to save books to CSV file
def save_books(books):
    with open(BOOKS_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Quantity"])
        writer.writeheader()
        writer.writerows(books)

# Function to display all books
def display_books(books):
    print("Available Books:")
    for book in books:
        print(f"{book['Title']} by {book['Author']} - Quantity: {book['Quantity']}")

# Function to search for a book by title or author
def search_book(books, search_term):
    found_books = []
    for book in books:
        if search_term.lower() in book['Title'].lower() or search_term.lower() in book['Author'].lower():
            found_books.append(book)
    return found_books

# Function to borrow a book
def borrow_book(books, user):
    display_books(books)
    title = input("Enter the title of the book you want to borrow: ")
    for book in books:
        if book['Title'].lower() == title.lower():
            if int(book['Quantity']) > 0:
                book['Quantity'] = str(int(book['Quantity']) - 1)
                print(f"{book['Title']} borrowed successfully by {user}.")
                return True
            else:
                print("Sorry, this book is currently out of stock.")
                return False
    print("Book not found.")
    return False

# Function to return a borrowed book
def return_book(books, user):
    borrowed_books = [book for book in books if int(book['Quantity']) < 5]  # Assuming borrowed books have quantity less than 5
    if borrowed_books:
        print("Borrowed Books:")
        for book in borrowed_books:
            print(f"{book['Title']} by {book['Author']}")
        title = input("Enter the title of the book you want to return: ")
        for book in borrowed_books:
            if book['Title'].lower() == title.lower():
                book['Quantity'] = str(int(book['Quantity']) + 1)
                print(f"{book['Title']} returned successfully by {user}.")
                return True
        print("Book not found in your borrowed books.")
    else:
        print("You haven't borrowed any books.")
    return False

# Function to view borrowed books by user
def view_borrowed_books(books, user):
    borrowed_books = [book for book in books if int(book['Quantity']) < 5]  # Assuming borrowed books have quantity less than 5
    if borrowed_books:
        print(f"Borrowed Books by {user}:")
        for book in borrowed_books:
            print(f"{book['Title']} by {book['Author']}")
    else:
        print(f"{user} hasn't borrowed any books.")

# Function for admin login
def admin_login():
    username = input("Enter admin username: ")
    password = getpass.getpass("Enter admin password: ")
    if username == "admin" and password == "password":
        return True
    else:
        print("Invalid username or password.")
        return False

# Main function
def main():
    print("Welcome to Library Management System!")
    books = load_books()
    user = input("Enter your name: ")
    while True:
        print("\nMenu:")
        print("1. Display all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View borrowed books")
        if admin_login():
            print("6. Add a new book")
            print("7. Quit")
        else:
            print("6. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_books(books)
        elif choice == "2":
            search_term = input("Enter the title or author of the book you want to search: ")
            found_books = search_book(books, search_term)
            if found_books:
                display_books(found_books)
            else:
                print("No matching books found.")
        elif choice == "3":
            borrow_book(books, user)
        elif choice == "4":
            return_book(books, user)
        elif choice == "5":
            view_borrowed_books(books, user)
        elif choice == "6" and admin_login():
            title = input("Enter the title of the new book: ")
            author = input("Enter the author of the new book: ")
            quantity = input("Enter the quantity of the new book: ")
            books.append({"Title": title, "Author": author, "Quantity": quantity})
            save_books(books)
            print("Book added successfully.")
        elif choice == "7" and admin_login():
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
