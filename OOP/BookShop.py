class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 3:
            raise ValueError('Title not valid!')
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if len(value.split()) < 2:
            raise ValueError('Price not valid!')
        elif any(char.isdigit() for char in value.split()[1]):
            raise ValueError('Author not valid!')
        self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError('Price not valid!')
        self.__price = value

    def __str__(self):
        return 'Type: ' + f'{type(self).__name__}' + '\n' + 'Title: ' + f'{self.title}' + '\n' + 'Author: ' + f'{self.author}' + '\n' + 'Price: ' + f'{self.price:.2f}'


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author, price)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if price <= 0:
            raise Exception('Price not valid!')
        self.__price = price + price * 0.30


try:
    price = float(input())
    author = input()
    title = input()


    book = Book(title, author, price)
    golden_edition_book = GoldenEditionBook(title=title, author=author, price=price)

    print(book)
    print()
    print(golden_edition_book)
except Exception as exe:
    print(exe)
