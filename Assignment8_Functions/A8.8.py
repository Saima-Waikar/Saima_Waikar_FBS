def fun():
    n = int(input("Enter a number:"))
    reverse = 0

    while n > 0:
        temp = n % 10
        n = n // 10
        reverse = reverse * 10 + temp

    print(reverse)

fun()