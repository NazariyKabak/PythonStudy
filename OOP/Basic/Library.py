class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"⚠ Книги '{book.get_title()}' немає в бібліотеці.")

    def printBooks(self):
        if not self.books:
            print("📚 Бібліотека порожня.")
        else:
            print("📚 Список книг:")
            for book in self.books:
                print(f"- {book.get_title()} ({book.get_author()}) - ${book.get_price()}")

