class Employee:
    def display(self):
        print("Employee details")


class HR(Employee):
    def display(self):
        print("HR details")


e = Employee()
h = HR()

e.display()
h.display()