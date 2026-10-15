import pickle

class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Salary:", self.salary)


emp = Employee(101, "Saima", 30000)

# Write object to file
f = open(r"D:\FBS\Core python\Demos\Basics\file\employee.dat", "wb")
pickle.dump(emp, f)
f.close()

print("Employee object added to file")


# Read object from file
f = open(r"D:\FBS\Core python\Demos\Basics\file\employee.dat", "rb")
emp1 = pickle.load(f)
f.close()

emp1.display()