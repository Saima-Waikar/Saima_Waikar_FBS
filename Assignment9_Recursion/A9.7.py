def sums(n, total=0):
    if n == 0:
        return total
    else:
        temp = n % 10
        return sums(n // 10, total + temp)


n = int(input("Enter a number: "))

res = sums(n)

print(res)