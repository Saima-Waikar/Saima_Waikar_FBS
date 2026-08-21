#1.To make parameter optional
#2.Parameter Defalut (Assigning value to parameter in function definition)
#3.If we pass value to default parameter,it takes passed value
  #If we dont pass value to default parameter,it takes default value
#4.Flow from right to left

def emp(id,name,salary,dept = "IT"):
    print("ID:",id)
    print("Name:",name)
    print("Salary:",salary)
    print("Department:",dept)

emp(101,'Saima',2000,"CSE")
emp(102,'Suzan',3000)


