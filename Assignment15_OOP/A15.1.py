class Book:
    def __init__(self,bid=0,bname="",bprice=0,bauthor=""):
        self.id = bid
        self.name = bname
        self.price = bprice
        self.author = bauthor
    def __del__(self):          #Destructor
        print("Book object deleted")
    def showbook(self):
        print(f"id={self.id}\tName={self.name}\tPrice={self.price}\tAuthor={self.author}")
b1=Book()                                   #parameterless
b2=Book(102,"Python Book",2000,"XYZ")       #parameterized
b1.showbook()
b2.showbook()