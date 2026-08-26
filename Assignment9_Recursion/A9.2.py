def armstrong(n, digits):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return digit ** digits + armstrong(n // 10, digits)


n = int(input("Enter a number: "))

digits = len(str(n))
res = armstrong(n, digits)

if res == n:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not armstrong number")