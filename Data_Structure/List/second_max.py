li = [19, 45, 32, 66, 99, 43, 27, 101]

max = li[0]
second_max = li[0]

for ind in range(1, len(li)):

    if li[ind] > max:
        second_max = max
        max = li[ind]

    elif li[ind] > second_max and li[ind] != max:
        second_max = li[ind]

print(f"Maximum number is: {max}")
print(f"Second maximum number is: {second_max}")