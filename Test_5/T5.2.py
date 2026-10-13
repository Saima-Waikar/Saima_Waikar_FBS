n = int(input("Enter number of coins: "))
L = list(map(int, input("Enter coin numbers: ").split()))

for i in L:
    if L.count(i) % 2 != 0:
        print("Missing coin number:", i)
        break