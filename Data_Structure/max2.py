li = [10, 20, 30]

max = li[0]
second_max = li[0]

for ind in range(1, len(li)):

    if li[ind] > max:
        second_max = max
        max = li[ind]

    elif li[ind] > second_max:
        second_max = li[ind]

print("Maximum:", max)
print("Second Maximum:", second_max)