class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def getdata(self):
        self.model_no = int(input("Enter model number: "))

        if self.model_no < 0 or self.model_no > 9999:
            raise ValueError("Model number must have at most 4 digits")

        self.screen_size = int(input("Enter screen size: "))

        if self.screen_size < 12 or self.screen_size > 70:
            raise ValueError("Screen size must be between 12 and 70 inches")

        self.price = float(input("Enter price: "))

        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000")

    def display(self):
        print("Model Number:", self.model_no)
        print("Screen Size:", self.screen_size, "inches")
        print("Price: Rs.", self.price)

    def setzero(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0


t = Television()

try:
    t.getdata()
except ValueError as e:
    print("Exception caught:", e)
    t.setzero()

t.display()