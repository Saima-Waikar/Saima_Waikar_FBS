li = [10, 20, 30, 20, 40, 10, 50, 30]

new_li = []

for i in li:
    if (i not in new_li):
        new_li.append(i)
print(new_li)