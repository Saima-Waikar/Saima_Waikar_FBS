li = [1,2,3,4,5,6,7,8,9]

target = 10

for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
            if(li[i] + li[j] + li[k] == target):
                print(li[i],li[j],li[k])