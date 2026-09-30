class Emp:
    def classsal(self):
        print("Emp")

class Hr(Emp):
    def classsal(self):
        print("Hr")

class Admin(Emp):
    pass
    #def classsal(self):
        #print("Admin")

h = Hr()
a = Admin()

h.classsal()
a.classsal()