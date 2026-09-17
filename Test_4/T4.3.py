for i in range(11):
    if i == 0 or i == 10:
        print("*" * 22)
    else:
        print(" " * (22 - i * 2) + "*")