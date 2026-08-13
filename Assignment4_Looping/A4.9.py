start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
n = int(input("Enter the number: "))

for i in range(start, end + 1):
    if (i % n == 0):
        print(i)