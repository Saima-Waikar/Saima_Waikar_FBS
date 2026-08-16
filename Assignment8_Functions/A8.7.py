def fun():
    n = int(input("Enter a number:"))
    sum = 0
    while(n>0):
        temp = n % 10
        n = n // 10
        sum = temp + sum
    print(f"Sum of digit is: {sum}")
fun()