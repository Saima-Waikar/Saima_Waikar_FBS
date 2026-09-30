class Book:
    count = 0

    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def __del__(self):
        Book.count -= 1

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)


# Parameterized constructor
b1 = Book(101, "Python", 500, "John")

# Parameterless constructor
b2 = Book()

b1.ShowBook()
b2.ShowBook()

print("Total Objects:", Book.count)