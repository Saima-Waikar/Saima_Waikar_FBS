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


s1 = Student(101, "Saima", 21, 85.5)

s1.Display()

print("Rank =", s1.CalculateRank())

print("Student =", s1)