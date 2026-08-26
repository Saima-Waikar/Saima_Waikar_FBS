def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        temp = n % 10
        rev = rev * 10 + temp
        return reverse(n // 10, rev)


n = int(input("Enter a number: "))

res = reverse(n)

print(res)