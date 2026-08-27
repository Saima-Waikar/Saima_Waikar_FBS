n = int(input("Enter number of elements to be put in the list:"))
li = [0] * n
even_li = []
odd_li = []
for i in range(n):
    li[i] = int(input("Enter element: "))
    if(li[i]%2==0):
        even_li.append(li[i])
    else:
        odd_li.append(li[i])
print(f"Original list : {li}")
print(f"Even list : {even_li}")
print(f"odd list : {odd_li}")