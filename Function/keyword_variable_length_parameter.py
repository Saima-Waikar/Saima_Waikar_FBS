#1.To pass multiple values with meaning function
#2.Use 2 * symbols before parameter name in function definition
#3.Passed data stored in dictonary format
#4.Use for loop on dict.items() to get values and keys

def emp(**data):
    for key,val in data.items():
        print(key,':',val)
        
emp(id=101,name="Saima",salary=50000,age=22)