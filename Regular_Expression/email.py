import re
email = input("Enter your mail:")
path = r"^[a-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
res = re.search(path,email)
if res:
    print("Pattern found")
else:
    print("Pattern not found")