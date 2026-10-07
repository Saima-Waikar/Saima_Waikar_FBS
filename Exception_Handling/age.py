try:
    age = int(input("Enter age:"))
    print(age)
except ValueError as v:                  #specialized exception
    print("Invalid value.",v)
except Exception as e:                   #generalized exception
    print(e)