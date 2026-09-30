class Employee:
    def __init__(self, eid, ename, esal):
        self.id = eid
        self.name = ename
        self.sal = esal

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal
    def setSal(self, newsal):
        self.sal = newsal

    def display(self):
        print(f"ID={self.id}\tName={self.name}\tSalary={self.sal}")

e1 = Employee(1, "Saima", 90000)

print(e1.getId())
print(e1.getName())
print(e1.getSal())

e1.setId(10)
e1.setName("Sam")
e1.setSal(95000)

e1.display()