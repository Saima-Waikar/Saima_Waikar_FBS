try:
    age=int(input("Enter age:"))
    if age>=0:
        raise ZeroDivisionError("Enter Valid age")
except Exception as e:
    print(e)