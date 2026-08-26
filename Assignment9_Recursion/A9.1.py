#1! + 2! + 3! + 4! +..... + n!
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def term(n):
    if n == 0:
        return 0
    else:
        return fact(n) + term(n - 1)


n = int(input("Enter n: "))

res = term(n)

print(f"Result of term is {res}")
        
    

