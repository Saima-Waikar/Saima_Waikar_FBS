n = 1

for i in range(1,11):
    if(i%2 != 0):
        for j in range(1,11):
            print(n,end=" ")
            n = n + 1
    else:
        n = n + 9
        for j in range(1,11):
            print(n,end=" ")
            n = n - 1
        n = n + 11
    print()