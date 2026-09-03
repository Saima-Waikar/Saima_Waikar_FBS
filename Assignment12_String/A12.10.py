str1 = input("Enter a string:")
str2 = input("Enter a string:")
count1 = 0
count2 = 0
for i in str1:
    count1 = count1 + 1
for j in str2:
    count2 = count2 + 1
if(count1>count2):
    print("Larger string:",str1)
elif(count1==count2):
    print("Both String are of equal length")
else:
    print("Larger string:",str2)

#if(len(str1)>len(str2)):
    #print(str1)
#else:
    #print(str2)