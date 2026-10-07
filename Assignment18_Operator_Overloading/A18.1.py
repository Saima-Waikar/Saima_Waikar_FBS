class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Object destroyed")

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = ComplexNumber(10, 5)
c2 = ComplexNumber(4, 2)

c3 = c1 + c2
print("Addition:", c3)

c4 = c1 - c2
print("Subtraction:", c4)