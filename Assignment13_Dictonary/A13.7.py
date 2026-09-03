dict = {1: 10, 2: 'B', 3: 30, 4: 'D'}

key = int(input("Enter a key: "))

new_dict = {}

for i in dict:
    if key == i:
        pass
    else:
        new_dict[i] = dict[i]

print(new_dict)