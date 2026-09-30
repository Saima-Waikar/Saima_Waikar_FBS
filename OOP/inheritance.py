class student():
    count = 0
    def __init__(self,eid,ename):
        self.id = eid
        self.name = ename
        student.count = student.count + 1
    def display(self):
        print(f"ID={self.id}\tName={self.name}")

class placedstudent(student):                #Inheritance
    def __init__(self,eid,ename,cname):
        super().__init__(eid,ename)          #super()-access the constructor of base class
        self.cname = cname
    def display(self):
        print(f"ID={self.id}\tName={self.name}\tCompany Name={self.cname}")
s1 = student(1,"Anjali")
s2 = student(2,"Sam")
s3 = placedstudent(3,"Saima","TCS")
s1.display()
s2.display()
s3.display()
print("Total count of students:",student.count)