li = [12,3,6,78,45,32,12,90]

max = li[0]
second_max = li[0]

for i in li:
    if(max<i):
        second_max = max
        max = i
    elif(second_max<i and i!=max):
        second_max = i
print(f"Second maximum element from list is: {second_max}")
