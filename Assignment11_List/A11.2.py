li1 = [10,30,50,20]
li2 = [40,80,60,70]

li3 = li1 + li2

for i in range(len(li3)):
    for j in range(i+1,len(li3)):
        if(li3[i] > li3[j]):
            li3[i], li3[j] = li3[j], li3[i]

print("Merged and sorted list:", li3)