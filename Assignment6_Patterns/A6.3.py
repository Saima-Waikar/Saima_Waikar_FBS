for i in range(1, 5):
    for j in range(1, 11 - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        if i == 3 and j == 2:
            print("  2", end=" ")
        elif i == 4 and (j == 2 or j == 3):
            print("  3", end=" ")
        else:
            print("  1", end=" ")

    print()