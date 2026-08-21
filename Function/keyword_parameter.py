#1.To neglect positional parameter
#2.Assign value to parameter in function call
#3.Parameter name in function definition and function call should be same
#4.Flow from right to left

def emp(id,name,salary,dept = "IT"):
    print("ID:",id)
    print("Name:",name)
    print("Salary:",salary)
    print("Department:",dept)

emp(name ='Saima', salary =2000,dept ="CSE",id =101)