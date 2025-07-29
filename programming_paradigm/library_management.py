class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        if not self._is_checked_out:
            self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []
        self.book = None

    def add_book(self, book: Book):
        if book is not None:
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                self.book = book
                self._books.remove(book)
                book.check_out()

    def return_book(self, title):
        for book in self._books:
            if book.title != title:
                self._books.append(self.book)
                self.book.return_book()

    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")
