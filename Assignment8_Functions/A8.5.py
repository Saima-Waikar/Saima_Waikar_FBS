def fun():
    n = int(input("Enter n: "))
    sum = 0

    for i in range(1, n + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1

        if count == 2:
            sum = i + sum

    print(f"Sum = {sum}")

fun()