try:
    a = int(input("Enter num1:"))
    b = int(input("Enter num2:"))
    print(a / b)

except ZeroDivisionError as a:                   #specialized exception
    print("Cannot divide by zero.",a)
except Exception as e:                          #generalized exception
    print(e)
else:
    print("No exception")                       #If no exception then else block executed