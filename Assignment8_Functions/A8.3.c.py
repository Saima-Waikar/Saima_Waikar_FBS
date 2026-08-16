#1^1 + 2^2 + 3^3+ ...... n^n
def fun():
    n = int(input("Enter n :"))
    sum = 0
    for i in range(1,n+1):
        term = i**i
        sum = sum + term
    print(f"Sum = {sum}")
fun()
    