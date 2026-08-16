def fun():
    n = int(input("Enter a number: "))
    original = n
    sum = 0
    digits = len(str(n))

    while (n > 0):
        temp = n % 10
        n = n // 10
        sum = sum + temp ** digits

    if (sum == original):
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

fun()