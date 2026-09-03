str = "Python Programming"
new_str = ""
for i in str:
    if(i==" "):
        new_str = new_str + "-"
    else:
        new_str = new_str + i
print(new_str)