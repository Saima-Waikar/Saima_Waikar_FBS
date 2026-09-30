class Emp:
    def __init__(self,id,name,sal):
        self.eid = id       #public:Everywhere in code
        self._name = name   #protected:Available in class and subclass
        self.__sal = sal    #private:Only avaliable in inside the class
    
e1=Emp(101,"Saima",6000000)

print(e1.eid)        #public-works
print(e1._name)      #protected-Not works in python because of name mangling
#print(e1.__sal)     #private-raise error
print(e1._Emp__sal)  #private-works like this