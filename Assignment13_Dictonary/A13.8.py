str = input("Enter a string: ")

words = str.split()
count = {}

for i in words:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

print(count)