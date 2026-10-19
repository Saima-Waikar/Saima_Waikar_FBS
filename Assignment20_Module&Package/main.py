from package.SY import SYMarks
from package.TY import TYMarks

class Student:
    def __init__(self, roll_no, name, SYMarks, TYMarks):
        self.roll_no = roll_no
        self.name = name
        self.sy = SYMarks
        self.ty = TYMarks

    def display(self):
        total = self.sy.c + self.ty.t + self.ty.p

        if total >= 70:
            grade = "A"
        elif total >= 60:
            grade = "B"
        elif total >= 50:
            grade = "C"
        elif total >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("SY Computer:", self.sy.c)
        print("TY Theory:", self.ty.t)
        print("TY Practical:", self.ty.p)
        print("Total:", total)
        print("Grade:", grade)


sy = SYMarks(88, 98, 78)
ty = TYMarks(42, 28)

s = Student(1, "Saima", sy, ty)
s.display()