class Shirt:
    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.id = sid
        self.name = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt object deleted")

    def Showshirt(self):
        print(f"id={self.id}\tName={self.name}\tType={self.type}\tPrice={self.price}\tSize={self.size}")

s1 = Shirt()
s2 = Shirt(101, "Formal Shirt", "Formal", 1200, "Large")
s1.Showshirt()
s2.Showshirt()