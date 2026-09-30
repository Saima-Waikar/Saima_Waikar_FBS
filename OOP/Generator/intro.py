def generateValues(n):
    for i in range(1,n+1):
        yield i

res = generateValues(5)
print(next(res))
print(next(res))
print(next(res))