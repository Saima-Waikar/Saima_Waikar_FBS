n = int(input("Enter n:"))
count = 0
num = 2
while count < n:
    fact = 0
    for i in range(1, num + 1):
        if num % i == 0:
            fact = fact + 1
    if fact == 2:
        print(num)
        count = count + 1
    num = num + 1