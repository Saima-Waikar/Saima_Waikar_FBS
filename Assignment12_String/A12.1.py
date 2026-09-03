s = input("Enter a string: ")

new = ""

for i in s:
    if i == 'a':
        new = new + '$'
    else:
        new = new + i

print(new)

#s = input("Enter a string: ")
#s = s.replace('a', '$')
#print(s)