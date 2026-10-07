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


class MedicalStudent(Student):

    def __init__(self, studentId, name, age, percentage, specialization, marksOfInternship):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    def Display(self):
        super().Display()
        print("Specialization =", self.specialization)
        print("Marks of Internship =", self.marksOfInternship)

    def Accept(self):
        super().Accept()
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(input("Enter Marks of Internship: "))

    def CalculateRank(self):
        total = self.percentage + self.marksOfInternship

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
        return f"{self.studentId} {self.name} {self.age} {self.percentage} {self.specialization} {self.marksOfInternship}"


m1 = MedicalStudent(102, "Ayesha", 22, 85, "Cardiology", 80)

m1.Display()
print("Rank =", m1.CalculateRank())
print(m1)