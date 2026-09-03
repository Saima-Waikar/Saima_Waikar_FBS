dict = {1: 'A', 2: 'B', 3:'C', 4:'D'}

key = int(input("Enter Key:"))

found = False

for i in dict:
    if i == key:
        print(f"{key} Key exists in dictionary")
        found = True
        break

if found == False:
    print(f"{key} Key doesn't exist in dictionary")