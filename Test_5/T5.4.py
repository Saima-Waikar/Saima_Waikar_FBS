L = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]
D = {}

for i in L:
    if i in D:
        D[i] = D[i] + 1
    else:
        D[i] = 1

print(D)