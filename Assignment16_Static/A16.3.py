class Shirt:
    price_increase = 10

    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt object destroyed")

    def ShowBook(self):
        final_price = self.price

        if self.size == "small":
            final_price = self.price
        elif self.size == "medium":
            final_price = self.price + (self.price * Shirt.price_increase / 100)
        elif self.size == "large":
            final_price = self.price + (self.price * Shirt.price_increase * 2 / 100)
        elif self.size == "xlarge":
            final_price = self.price + (self.price * Shirt.price_increase * 3 / 100)

        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", final_price)
        print("Size:", self.size)


# Parameterized constructor
s1 = Shirt(101, "Formal Shirt", "Formal", 1000, "small")
s2 = Shirt(102, "Formal Shirt", "Formal", 1000, "medium")
s3 = Shirt(103, "Formal Shirt", "Formal", 1000, "large")
s4 = Shirt(104, "Formal Shirt", "Formal", 1000, "xlarge")

s1.ShowBook()
print()
s2.ShowBook()
print()
s3.ShowBook()
print()
s4.ShowBook()