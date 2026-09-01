li = [20,30,10,40,10]

li.append(50)
print(li)

li2 = li.copy()
print(li2)

print(li.count(10))

li.extend([60,70,80])
print(li)

print(li.index(40))

li.insert(2,50)
print(li)

li.pop(1)
print(li)

li.remove(20)
print(li)

li.reverse()
print(li)

li.sort()
print(li)

li.sort(reverse=True)
print(li)

li.clear()
print(li)