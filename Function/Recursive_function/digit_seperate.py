def separate(n):
    if n == 0:
        return
    else:
        separate(n // 10)
        print(n % 10)

n = int(input("Enter number: "))
separate(n)