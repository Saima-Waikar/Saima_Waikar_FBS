def fun():
    n = int(input("Enter a number: "))
    original = n
    reverse = 0

    while n > 0:
        temp = n % 10
        n = n // 10
        reverse = reverse * 10 + temp

    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

fun()