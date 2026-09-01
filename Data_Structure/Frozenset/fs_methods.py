S1 = frozenset({10, 20, 30, 40})
S2 = frozenset({30, 40, 50, 60})
S3 = frozenset({50, 60})
S4 = frozenset({50, 60})

print(S1.copy())

print(S1.difference(S2))

print(S1.intersection(S2))

print(S1.isdisjoint(S3))

print(S3.issubset(S2))

print(S2.issuperset(S3))

print(S1.symmetric_difference(S2))

print(S1.union(S2))