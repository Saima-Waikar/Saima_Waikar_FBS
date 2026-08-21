#with passing parameter (with input)
#with returning parameter (with output)

def addition(num1,num2):

     add = num1+num2
     return add

num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))

result = addition(num1,num2)
print(result)