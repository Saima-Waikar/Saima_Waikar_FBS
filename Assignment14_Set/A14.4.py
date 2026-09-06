li = [2,5,3,4,6,1,7,8,9]
n = int(input("Enter a value:"))
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if (li[i]+li[j] == n):
            print(li[i],li[j])