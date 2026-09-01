li = [[1,5],[2,3],[3,8],[4,2]]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(li[i][1] > li[j][1]):
            li[i],li[j] = li[j],li[i]

print("Sorted list:",li)