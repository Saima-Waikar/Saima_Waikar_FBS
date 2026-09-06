li = [2,3,4,5,6,1,7,8,9]
s = set()
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        s.add((li[i]*li[j],li[i],li[j]))
x = max(s)
print(x[1],x[2])