def prime(n, i=2):
    if n <= 1:
        return False
    elif i == n:
        return True
    elif n % i == 0:
        return False
    else:
        return prime(n, i + 1)


n = int(input("Enter a number: "))
res = prime(n)

print(res)