class Student:

    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def __str__(self):
        return f"{self.studentId} {self.name} {self.age} {self.percentage}"


class College:

    def __init__(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents
        self.students = []

    def AddStudent(self, student):
        if len(self.students) < self.numberOfStudents:
            self.students.append(student)

    def GetStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                return student
        return None

    def RemoveStudent(self, studentId):
        student = self.GetStudent(studentId)

        if student is not None:
            self.students.remove(student)

    def __str__(self):
        result = ""

        for student in self.students:
            result = result + str(student) + "\n"

        return result


s1 = Student(101, "Saima", 21, 85)
s2 = Student(102, "Sam", 22, 78)

c1 = College(3)

c1.AddStudent(s1)
c1.AddStudent(s2)

print(c1)

print("Get Student:")
print(c1.GetStudent(101))

c1.RemoveStudent(102)

print("After Remove:")
print(c1)