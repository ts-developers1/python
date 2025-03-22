import json
import os

# File to store book data
BOOKS_FILE = "books.json"

class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        """Load books from file or return a default book list"""
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r") as file:
                return json.load(file)
        else:
            return [
                {"title": "Python Crash Course", "author": "Eric Matthes", "available": True},
                {"title": "The Pragmatic Programmer", "author": "Andy Hunt", "available": True},
                {"title": "Clean Code", "author": "Robert C. Martin", "available": True},
            ]

    def save_books(self):
        """Save books to file"""
        with open(BOOKS_FILE, "w") as file:
            json.dump(self.books, file, indent=4)

    def display_books(self):
        """Display all available books"""
        print("\n📚 Available Books:")
        for i, book in enumerate(self.books, start=1):
            status = "✅ Available" if book["available"] else "❌ Not Available"
            print(f"{i}. {book['title']} by {book['author']} - {status}")

    def borrow_book(self, title):
        """Borrow a book if available"""
        for book in self.books:
            if book["title"].lower() == title.lower() and book["available"]:
                book["available"] = False
                self.save_books()
                print(f"\n📖 You have borrowed '{book['title']}'!")
                return
        print("\n⚠ Book not available or does not exist!")

    def return_book(self, title):
        """Return a borrowed book"""
        for book in self.books:
            if book["title"].lower() == title.lower() and not book["available"]:
                book["available"] = True
                self.save_books()
                print(f"\n🔄 You have returned '{book['title']}'!")
                return
        print("\n⚠ Invalid return request!")

    def add_book(self, title, author):
        """Add a new book to the library"""
        self.books.append({"title": title, "author": author, "available": True})
        self.save_books()
        print(f"\n✅ '{title}' by {author} added to the library!")

def main():
    library = Library()

    while True:
        print("\n📚 Library Management System")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add New Book")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("\nEnter book title to borrow: ")
            library.borrow_book(title)
        elif choice == "3":
            title = input("\nEnter book title to return: ")
            library.return_book(title)
        elif choice == "4":
            title = input("\nEnter new book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)
        elif choice == "5":
            print("\n📕 Exiting Library System. Goodbye!")
            break
        else:
            print("\n⚠ Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
