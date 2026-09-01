li = ["apple","cat","banana","hi"]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(len(li[i]) > len(li[j])):
            li[i],li[j] = li[j],li[i]

print("Sorted list:",li)