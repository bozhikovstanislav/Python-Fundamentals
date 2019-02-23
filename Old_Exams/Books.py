class BookStore:
    def __init__(self, book):
        self.booklst = book


class Book:
    def __init__(self, title, author, chapter, price):
        self.title = title
        self.author = author
        self.chapter = list(chapter)
        self.price = int(price)


book1 = Book("han kubrat", "Tangra", ['1', '3', '4', '2'], 1)
book2 = Book("han Asparuh", "Vitosha", ['12', '123', '55', '22'], 2)
book3 = Book("han Tervel", "StaraPlanina", ['155', '33', '41', '245'], 3)

lst_book = [book1, book2, book3]
bookstor = BookStore(lst_book)
