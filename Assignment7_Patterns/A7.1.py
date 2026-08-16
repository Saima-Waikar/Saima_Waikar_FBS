for i in range(1,6):
    for j in range(1,7-i):
        print(" ", end=" ")

    for j in range(1,i+1):
        if j == 1:
            print("*", end=" ")

    for j in range(1,2*i-2):
        print(" ", end=" ")

    for j in range(1,i+1):
        if j == i and i > 1:
            print("*", end=" ")

    print()


for i in range(4,0,-1):
    for j in range(1,7-i):
        print(" ", end=" ")

    for j in range(1,i+1):
        if j == 1:
            print("*", end=" ")

    for j in range(1,2*i-2):
        print(" ", end=" ")

    for j in range(1,i+1):
        if j == i and i > 1:
            print("*", end=" ")

    print()