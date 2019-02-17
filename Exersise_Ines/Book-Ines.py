# class Book:
#     def __init__(self, title, author, pages, pub_date, chapters):
#         self.title = title
#         self.author = self.set_author(author)
#         self.pages = self.set_pages(pages)
#         self.pub_date = self.set_pub_date(pub_date)
#         self.chapters = self.set_chapters(chapters)
#
#     def set_chapters(self, chapters):
#         c = len(chapters)
#         if c >= 1:
#             return chapters
#         raise Exception
#
#     def set_pub_date(self, pub_date):
#         l = len(list(pub_date.split('-')))
#         if l == 3:
#             return pub_date
#         raise Exception
#
#     def set_pages(self, pages):
#         if isinstance(pages, int):
#             return pages
#
#     def set_author(self, author):
#         if isinstance(author, str):
#             return author
#         raise Exception('Author must be string')
#
#     def __str__(self):
#         return f'Tile: {self.title}, with author {self.author}, number of pages: {self.pages}\nPublished at {self.pub_date}\nChapters: {", ".join(
#         self.chapters)}'
#
#         data = input()
#         books_store = []
#
#
# while not data == 'end':
#     splitted_data = data.split(" ")
#     title = splitted_data[0]
#     author = splitted_data[1]
#     pages = int(splitted_data[2])
#     pub_date = splitted_data[3]
#     chapters = splitted_data[4].split(",")
#
#     try:
#         book = Book(title, author, pages, pub_date, chapters)
#         books_store.append(book)
#     except:
#         pass
#
#     data = input()
#
# sorted_book_store = sorted(books_store, key=lambda book: (-len(book.chapters), book.title))
# for book in sorted_book_store:
