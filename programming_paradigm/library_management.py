class Book:
    def __init__(self,title,author):
        self.title = title 
        self.author = author
        self._is_checked_out = False

        def __str__(self):
            return f"{self.title} by {self.author}"

class Library:
    def __init__(self):

        self._books = [
            Book(title="Brave New World",author="by Aldous Huxley"), 
            Book(title="1984",author="by George Orwell")
        ]
    def Initial_list_of_available_books(self):
        return f"Available books after setup:\n" + "\n".join(str(book) for book in self._books)

    def add_book(self):
        new_book = Book()
        self._books.append(new_book)

    def check_out_book(self,title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return f"Available books after checking out '{book.title}'."
        return f"'{title}' is not available for checkout."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return f"You have returned '{book.title}'."
        return f"'{title}' was not checked out."

    def list_checked_out_books(self):
        checked_out_books = [str(book) for book in self._books if book._is_checked_out]
        return "Checked out books:\n" + "\n".join(checked_out_books) if checked_out_books else "No books are currently checked out."