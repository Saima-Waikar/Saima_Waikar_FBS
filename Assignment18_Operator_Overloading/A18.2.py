class Distance:

    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print("Object destroyed")

    def __add__(self, other):
        cm = self.cm + other.cm
        m = self.m + other.m
        km = self.km + other.km

        if cm >= 100:
            m += cm // 100
            cm = cm % 100

        if m >= 1000:
            km += m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        total = total1 - total2

        km = total // 100000
        total = total % 100000

        m = total // 100
        cm = total % 100

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"


d1 = Distance(5, 600, 80)
d2 = Distance(2, 500, 40)

d3 = d1 + d2
print("Addition:", d3)

d4 = d1 - d2
print("Subtraction:", d4)