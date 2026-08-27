n = int(input("Enter number of elements to be put in the list:"))
li = [0] * n
new_li = []
for i in range(n):
    li[i] = int(input("Enter element:"))
print("Original list:", li)
k = int(input("Enter element to be searched:"))
for i in range(n):
    if(li[i] != k):
        new_li.append(li[i])
print("List after removing all occurrences:", new_li)
