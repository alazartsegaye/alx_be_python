class Book:
    """
    Base class representing a book.
    """
    def __init__(self, title, author):
        """
        Initialize a book with a title and an author.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of a book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book (EBook).
    """
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook with title, author, and file size in KB.
        """
        self.file_size = file_size
        super().__init__(title, author)

    def __str__(self):
        """
        String representation of an EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a printed book.
    """
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook with title, author, and number of pages.
        """
        self.page_count = page_count
        super().__init__(title, author)

    def __str__(self):
        """
        String representation of a PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Class representing a library that stores books.
    """
    def __init__(self):
        """
        Initialize the library with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        List all books in the library.
        """
        for book in self.books:
            print(book)