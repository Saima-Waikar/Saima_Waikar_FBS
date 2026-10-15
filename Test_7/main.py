
from book import Book

books = {}

while True:
    print("\n1. Add Book")
    print("2. Delete Book")
    print("3. Display All Books")
    print("4. Search Book")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        bid = int(input("Enter book id: "))
        name = input("Enter book name: ")
        price = float(input("Enter price: "))
        author = input("Enter author name: ")

        b = Book(bid, name, price, author)
        books[bid] = b
        print("Book added successfully")

    elif ch == 2:
        bid = int(input("Enter book id to delete: "))

        if bid in books:
            del books[bid]
            print("Book deleted successfully")
        else:
            print("Book not found")

    elif ch == 3:
        for bid, b in books.items():
            print("ID:", b.bid)
            print("Name:", b.name)
            print("Price:", b.price)
            print("Author:", b.author)

    elif ch == 4:
        bid = int(input("Enter book id to search: "))

        if bid in books:
            b = books[bid]
            print("ID:", b.bid)
            print("Name:", b.name)
            print("Price:", b.price)
            print("Author:", b.author)
        else:
            print("Book not found")

    elif ch == 5:
        break

    else:
        print("Invalid choice")
