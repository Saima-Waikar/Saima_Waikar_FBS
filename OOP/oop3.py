class A:
    def add(self):
        print("add A")

class B:
    def add(self):
        print("add B")

class C(B,A):
    def add(self):
        print("add C")

c1 = C()
c1.add()