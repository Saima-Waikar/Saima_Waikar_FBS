#1.To pass multiple values to function
#2.Mention 1 * symbol before parameter name in function definition
#3.Passed values are stored in tuple format
#4.Use for loop to iterate values from tuple

def add(*data):
    sum = 0 
    for val in data:
        sum += val
    return sum
result = add(12,34,56,3,4,5,2,3,22,3,45,67,32,98,766,54)
print(result)
