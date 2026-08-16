#1+ 2 + 3 + 4+..... + n
def fun():
    n = int(input("Enter n :"))
    sum = 0
    for i in range(1,n+1):
        sum = i+sum
    print(f"Sum = {sum}")
fun()
