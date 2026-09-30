class Product:
    discount = 10

    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product object destroyed")

    def ShowBook(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def apply_discount(self):
        self.price = self.price - (self.price * Product.discount / 100)


# Parameterized constructor
p1 = Product(101, "Laptop", 50000, 2)

# Parameterless constructor
p2 = Product()

print("Before Discount:")
p1.ShowBook()

p1.apply_discount()

print("\nAfter Discount:")
p1.ShowBook()