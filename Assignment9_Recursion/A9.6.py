def fibonacci(n,a,b):
    if(n==0):
        return 0
    else:
        return fibonacci(c = a + b) 

n = int(input("Enter n:"))
a = 0
b = 1
res = fibonacci(n,a,b)
print(res)