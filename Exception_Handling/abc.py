from myexception import MyException

try:
    age = int(input("Enter your age: "))

    if age <= 0:
        raise MyException(age)

    print(f"Valid age: {age}")

except MyException as e:
    print(e)

except ValueError:
    print("Please enter a valid number.")