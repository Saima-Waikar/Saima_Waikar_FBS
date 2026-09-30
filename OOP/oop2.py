class Employee:
    def __init__(self, eid, ename, esal):          #Constructor
        self.id = eid
        self.name = ename
        self.sal = esal
    def display(self):
            print(f"ID={self.id}\tName={self.name}\tSalary={self.sal}")
e1=Employee(1,"Saima",90000)
e2=Employee(2,"Sam",60000)
e1.display()
e2.display()