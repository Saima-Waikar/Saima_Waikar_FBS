class Student:
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def Display(self):
        print("Student ID =", self.studentId)
        print("Name =", self.name)
        print("Age =", self.age)
        print("Percentage =", self.percentage)

    def Accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        elif self.percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.studentId} {self.name} {self.age} {self.percentage}"


class EnggStudent(Student):

    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def Display(self):
        super().Display()
        print("Branch =", self.branch)
        print("Internal Marks =", self.internalMarks)

    def Accept(self):
        super().Accept()
        self.branch = input("Enter Branch: ")
        self.internalMarks = float(input("Enter Internal Marks: "))

    def CalculateRank(self):
        total = self.percentage + self.internalMarks

        if total >= 160:
            return "Distinction"
        elif total >= 130:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.studentId} {self.name} {self.age} {self.percentage} {self.branch} {self.internalMarks}"


e1 = EnggStudent(101, "Saima", 21, 85, "CSE", 80)

e1.Display()
print("Rank =", e1.CalculateRank())
print(e1)