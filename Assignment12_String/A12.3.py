str1 = input("Enter String1: ")
str2 = input("Enter String2: ")

for i in range(len(str1)):                                                  #str1[:j]       # before the two characters
    for j in range(len(str1)-1):                                            #str1[j+1]      # second character first
        if str1[j] > str1[j+1]:                                             #str1[j]        # first character second
            str1 = str1[:j] + str1[j+1] + str1[j] + str1[j+2:]              #str1[j+2:]     # remaining characters
for i in range(len(str2)):
    for j in range(len(str2)-1):
        if str2[j] > str2[j+1]:
            str2 = str2[:j] + str2[j+1] + str2[j] + str2[j+2:]

if str1 == str2:
    print("String is anagram")
else:
    print("String is not anagram")

#if sorted(str1) == sorted(str2):
    #print("String is anagram")
#else:
    #print("String is not anagram")