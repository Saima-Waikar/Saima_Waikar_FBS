li = [10,34,56,32,9,87,77]
max = li[0]
min = li[0]
for i in li:
    if(max<i):
        max = i
    elif(min>i):
        min = i
print(f"Maximum element from list is :{max}")
print(f"Minimum element from list is :{min}")
