n = int(input("Enter number of elements to be put in the list:"))
li = [0] * n
square_li = []
cube_li = []
for i in range(n):
    li[i] = int(input("Enter element: "))
print(f"Original list:{li}")
for i in range(n):
    square_li.append(li[i]**2)
    cube_li.append(li[i]**3)
print(f"Square list: {square_li}")
print(f"Cube list: {cube_li}")
    