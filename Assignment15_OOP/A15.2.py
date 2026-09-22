class Product:
    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.id = pid
        self.name = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product object deleted")

    def Showproduct(self):
        print(f"id={self.id}\tName={self.name}\tPrice={self.price}\tQuantity={self.quantity}")

p1 = Product()
p2 = Product(102, "Laptop", 50000, 2)
p1.Showproduct()
p2.Showproduct()