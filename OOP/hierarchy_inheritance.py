class Employee:
    def display(self):
        print("Employee details")


class HR(Employee):
    def work(self):
        print("HR manages employees")


class Admin(Employee):
    def work(self):
        print("Admin manages company operations")


class Developer(Employee):
    def work(self):
        print("Developer develops software")


h = HR()
a = Admin()
d = Developer()

h.display()
h.work()

a.display()
a.work()

d.display()
d.work()