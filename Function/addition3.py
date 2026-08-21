#without passing parameter (without input)
#with returning parameter (with output)

def addition():
    num1 = int(input('Enter a number1:'))
    num2 = int(input('Enter a number2:'))

    add = num1+num2

    return add

result = addition()
print(result)