di = {1: 'Python', 2: 'Java', 3: 'C'}

di2 = di.copy()
print(di)

print(di.get(4, 'Key not exists'))
#print(di[4])   raise error if key not exists

print(di.items())

print(di.keys())

di.pop(2)
print(di)

di.popitem()
print(di)

di.update({4: 'Go', 5: 'R'})
print(di)

print(di.values())

di.clear()
print(di)