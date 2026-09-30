class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSal(self):
        return self.sal

    def setSal(self, newsal):
        self.sal = newsal

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def display(self):
        print(f"id={self.id}\tName={self.name}\tSal={self.sal}")

    def calSal(self):
        print("Emp Sal=", self.sal)


# Emp Ends here............................

class Hr(Employee):
    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.com = com

    def getCom(self):
        return self.com

    def setCom(self, newcom):
        self.com = newcom

    # Polymorphism
    def calSal(self):
        print(f"Final HR Sal={self.com + self.getSal()}")


# Hr Ends here............................

class Dev(Employee):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def setBonus(self, newbon):
        self.bonus = newbon

    # Polymorphism
    def calSal(self):
        print(f"Final Dev Sal={self.bonus + self.getSal()}")


# Developer Ends here............................

e1=Employee(12,"Sachin",900999)
h1=Hr(18,"Smriti",85669,1000)
d=Dev(1,"Pravin",89650,100)
e1.calSal()
h1.calSal()
d.calSal()