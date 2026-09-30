class Employee:
    def display(self):
        print("Employee details")


class HR(Employee):
    def recruit(self):
        print("HR recruits employees")


class JrHR(HR):
    def interview(self):
        print("JrHR conducts interviews")


j = JrHR()

j.display()
j.recruit()
j.interview()