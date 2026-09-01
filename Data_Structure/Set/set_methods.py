S1 = {10, 20, 30, 40}
S2 = {30, 40, 50, 60}
S3 = {50, 60}
S4 = {50, 60}

S1.add(70)
print(S1)

S5 = S1.copy()
print(S5)

print(S1.difference(S2))

S1.difference_update(S2)
print(S1)

S1.discard(50)
print(S1)

print(S1.intersection(S2))

S1.intersection_update(S2)
print(S1)

print(S1.isdisjoint(S3))

print(S3.issubset(S2))

print(S2.issuperset(S3))

print(S1.symmetric_difference(S2))

S1.symmetric_difference_update(S2)
print(S1)

print(S1.union(S2))

S1.update({70,80,90})
S1.update(S2)
print(S1)

print(S1.pop())
print(S1)

S1.remove(30)
print(S1)

S1.clear()
print(S1)