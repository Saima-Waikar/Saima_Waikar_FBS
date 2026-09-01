li = [10,20,31,40,51,60,70,81,90]
even_li = []
odd_li = []
for i in li:
    if(i%2==0):
        even_li.append(i)
    else:
        odd_li.append(i)
print(f"Even list: {even_li}")
print(f"Odd list: {odd_li}")
