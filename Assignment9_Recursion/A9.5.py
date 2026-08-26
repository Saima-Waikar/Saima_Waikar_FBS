def factorial(n, fact=1):
    if n == 0 or n == 1:
        return fact
    else:
        return factorial(n - 1, fact * n)


n = int(input("Enter number: "))

res = factorial(n)

print(res)