def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)


m = int(input("Enter m: "))
n = int(input("Enter n: "))

res = power(m, n)

print(f"m to the n power is {res}")