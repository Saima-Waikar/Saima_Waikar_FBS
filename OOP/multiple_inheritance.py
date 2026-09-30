class Mechanical:
    def mechanical_work(self):
        print("Mechanical work")


class Electrical:
    def electrical_work(self):
        print("Electrical work")


class Mechatronics(Mechanical, Electrical):
    def mechatronics_work(self):
        print("Mechatronics work")


m = Mechatronics()

m.mechanical_work()
m.electrical_work()
m.mechatronics_work()