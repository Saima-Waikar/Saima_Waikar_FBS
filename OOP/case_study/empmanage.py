from hr import Hr
from dev import Dev
class EmpManage:
    Empdetil={}
    def addEmp(self):
        eid=input("Enter  Emp Id ")
        if eid in EmpManage.Empdetil:
            print("Employee is Aalredy Exist...")
            return
        else:
            ename=input("Enter the EMp  Name= ")
            esal=float(input("Eneter Emp  sal "))
            print("1.Hr")
            print("2.Devloper ")
            ch=int(input("Enter the Choice= "))
            if ch==1:
                ecom=float(input("enter the com of Hr= "))
                emp=Hr(eid,ename,esal,ecom)
            elif ch==2:
                bonus=float(input("enter the Bonus of Dev= "))
                emp=Dev(eid,ename,esal,bonus)
            else:
                print("Inavaldi choice ")
                return
            EmpManage.Empdetil[eid]=emp
            print("Emp added sussefully....")


    def displyEmp(self):
        if len(EmpManage.Empdetil)==0:
            print("Emp is not Exist,..... ")
        else:
            for var in EmpManage.Empdetil.values():
                print(var)


    def searchEmp(self):
        eid=input("Eneter the id of Employee to search employee ")
        if eid in EmpManage.Empdetil:
            print(EmpManage.Empdetil[eid])
        else:
            print("Employee is not Exist... ")


    def UpdateEmp(self):
        eid=input("Eneter the id of Employee to search employee ")
        if eid not in EmpManage.Empdetil:
            print("Employee not found,...")
            return
        else:
            emp=EmpManage.Empdetil[eid]
            print("1.Update Dev")
            print("2.Update Hr")
            ch=int(input("Enter the Choice="))
            if ch==1 and isinstance(emp,Dev):
                newname=input("Eneter new name of Dev")
                emp.setName(newname)
            elif ch==2 and isinstance(emp,Hr):
                newname=input("Eneter new name of Hr")
                emp.setName(newname)
            else:
                print("Type miamatched OR Invalid input")


    def deleteEmp(self):
        eid=input("Eneter the id of Employee to serch employee ")
        if eid in EmpManage.Empdetil:
            del EmpManage.Empdetil[eid]
            print("Employee deleted susefully...")
        else:
            print("Employee is not available")
    