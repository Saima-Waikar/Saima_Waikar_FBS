li = [19,45,32,66,99,43,27]

max = li[0]
for ind in range(1,len(li)):
    if(li[ind]>max):
        max = li[ind]
print(f"Maximum number is: {max}")
