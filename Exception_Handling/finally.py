try:
    a = int(input("Enter num1:"))
    b = int(input("Enter num2:"))
    print(a / b)

except ZeroDivisionError as a:                   #specialized exception
    print("Cannot divide by zero.",a)
except Exception as e:                          #generalized exception
    print(e)
finally:
    print("I am in finally block")              #Always executed finally block