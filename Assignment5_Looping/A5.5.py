for i in range(2, 101):
    count = 0

    for n in range(1, i + 1):
        if i % n == 0:
            count = count + 1

    if count == 2:
        print(i)