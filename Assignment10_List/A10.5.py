li = [10, 23, 56, 78, 98, 65, 43, 10]

n = int(input("Enter element to be checked in the list: "))

count = 0

for i in range(0, len(li)):
    if n == li[i]:
        count = count + 1

if count > 0:
    print(f"{n} element is present in the list")
    print(f"{n} is present {count} times in the list")
else:
    print(f"{n} element is not present in the list")