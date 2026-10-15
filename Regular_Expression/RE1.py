import re

# 1. re.match()
s = "Python is easy"
print(re.match("Python", s))
print(re.match("easy", s))

# 2. re.search()
s = "Python is easy"
print(re.search("easy", s))

# 3. re.findall()
s = "My numbers are 10, 20, 30"
print(re.findall(r"\d", s))
print(re.findall(r"\d+", s))

# 4. re.finditer()
s = "cat bat rat"
for i in re.finditer("at", s):
    print(i.group())

# 5. re.split()
s = "apple,banana;orange"
print(re.split(r"[,;]", s))

# 6. re.sub()
s = "I like Java"
print(re.sub("Java", "Python", s))

# 7. re.fullmatch()
print(re.fullmatch(r"\d+", "123"))
print(re.fullmatch(r"\d+", "123abc"))