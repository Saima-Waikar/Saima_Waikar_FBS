num = int(input("Enter number of elements to be put in the list:"))
li = [0] * num
new_li = []
for i in range(num):
    li[i] = int(input("Enter element: "))
print(f"original list: {li}")
m = int(input("Enter m:"))
n = int(input("Enter n:"))
for i in range(num):
    if(li[i]%m==0 and li[i]%n==0):
        new_li.append(li[i])
print(f"The list which is divisible by m and n {new_li}")