class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found in the library.")

    def display_books(self):
        for book in self.books:
            availability = "Available" if book.is_available else "Not Available"
            print(
                f"Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nAvailability: {availability}\n"
            )

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            print(f"You have borrowed '{book.title}'. Enjoy reading!")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")

    def return_book(self, book):
        if not book.is_available:
            book.is_available = True
            print(f"You have returned '{book.title}'. Thank you!")
        else:
            print("This book is already available in the library.")

    def save_books_to_file(self, filename):
        with open(filename, "w") as file:
            for book in self.books:
                file.write(
                    f"{book.title},{book.author},{book.genre},{book.is_available}\n"
                )

    def load_books_from_file(self, filename):
        self.books = []
        with open(filename, "r") as file:
            for line in file:
                book_data = line.strip().split(",")
                title, author, genre, is_available = book_data
                book = Book(title, author, genre)
                book.is_available = True if is_available == "True" else False
                self.add_book(book)


my_library = Library()

book1 = Book("Black Sheep", "Rachel Harrison", "Fiction")
book2 = Book("Alice", "Christina Henry", "Dark")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")

# my_library.add_book(book1)
# my_library.add_book(book2)
# my_library.add_book(book3)

# my_library.display_books()

# my_library.save_books_to_file("books.txt")

# my_library.remove_book(book1)

# my_library.display_books()

# book_to_borrow = my_library.find_book("Alice")
# my_library.borrow_book(book_to_borrow)


# book_to_return = my_library.find_book("Alice")
# my_library.return_book(book_to_return)

# my_library.display_books()

# my_library.return_book(book2)
# my_library.display_books()


my_library.load_books_from_file("books.txt")
my_library.display_books()
