class Library:

    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(self.book_name, "checked out successfully.")
        else:
            print(self.book_name, "is currently not available.")

    def return_book(self):
        self.available = True
        print(self.book_name, "returned successfully.")

    def display_book(self):
        status = "Available" if self.available else "Not Available"
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)


# Creating objects
book1 = Library("Python Programming", "James Smith")
book2 = Library("Machine Learning Basics", "David Brown")

# Display books
book1.display_book()
print()
book2.display_book()

print("\nChecking out book1:")
book1.check_out()

print("\nReturning book1:")
book1.return_book()

print("\nDisplaying book1 again:")
book1.display_book()