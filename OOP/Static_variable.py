class student:
    iname = "FBS"                  #Static variable
    def __init__(self,eid,ename,ebatch):
        self.id = eid
        self.name = ename
        self.batch = ebatch
    def display(self):
        print(f"Id:{self.id}\tName:{self.name}\tBatch:{self.batch}\tInstitute Name:{student.iname}")
s1 = student(1,"Saima","July")
s2 = student(2,"Sam","August")
s3 = student(3,"Rahul","September")
s1.display()
s2.display()
s3.display()
student.iname = "First Bit Solutions"              #static variable
s1.display()
s2.display()
s3.display()