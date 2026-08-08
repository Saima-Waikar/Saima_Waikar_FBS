x = 10
y = 10           #immutable - reuse
z = 20
li1 = [10, 20]
li2 = [10, 20]   #mutable - new memory

print(x is y)
print(x is z)
print(li1 is li2)
print(x is not z)